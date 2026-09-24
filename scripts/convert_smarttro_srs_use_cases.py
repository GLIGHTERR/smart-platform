#!/usr/bin/env python3
"""Recover SmartTrọ SRS use-case tables that are nested inside the DOCX.

The original Markdown conversion only visited top-level ``python-docx`` tables.
The SmartTrọ SRS stores its use-case catalogue and detailed specifications in
nested Word tables, so those sections were silently omitted.  This converter
uses the raw WordprocessingML document tree and emits a traceable baseline:

* the complete 33-row use-case catalogue in the main SRS mirror;
* one Markdown file for each of the 31 detailed specification tables actually
  present in the source document; and
* explicit warnings for the numbering/content inconsistencies in the source.

It intentionally does not modify the approved implementation specifications in
``docs/use-cases/smarttro``.
"""

from __future__ import annotations

import hashlib
import re
import unicodedata
from dataclasses import dataclass
from pathlib import Path
from xml.etree import ElementTree as ET
from zipfile import ZipFile


REPO_ROOT = Path(__file__).resolve().parents[1]
SOURCE = REPO_ROOT / "SRS" / "SRS (SmartTrọ).docx"
MAIN_MIRROR = REPO_ROOT / "markdown" / "SRS" / "SRS (SmartTrọ).md"
OUTPUT_DIR = REPO_ROOT / "markdown" / "SRS" / "use-cases"
CONVERSION_DATE = "2026-09-24"

W_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
W = f"{{{W_NS}}}"

EXPECTED_CATALOGUE_ROWS = 33
EXPECTED_DETAIL_TABLES = 31
EXPECTED_SOURCE_HASH = (
    "8cfae5992ace32ba2a206e879ce3ced370a526cf5d96cbb708f6157b94173d34"
)

SECTION_START = "## 3. Phân tích các Use Case / Use cases analysis"
SECTION_END = "## 4. Môi trường hoạt động / Operating Environment"

APPROVED_IMPLEMENTATION_DOCS = {
    1: "../../../docs/use-cases/smarttro/UC-01-sign-up.md",
    2: "../../../docs/use-cases/smarttro/UC-02-sign-in.md",
    3: "../../../docs/use-cases/smarttro/UC-03-forgot-password.md",
}

SUPPLEMENTAL_ACTIVITY_DIAGRAM_DOCS = [
    (
        "UC-6",
        "Tạo mới chữ ký điện tử",
        "../../../docs/use-cases/smarttro/UC-06-create-digital-signature.md",
    ),
    (
        "UC-7",
        "Cập nhật chữ ký điện tử",
        "../../../docs/use-cases/smarttro/UC-07-update-digital-signature.md",
    ),
]


@dataclass(frozen=True)
class Paragraph:
    text: str
    numbered: bool


@dataclass(frozen=True)
class DetailSection:
    section_number: str
    heading_id: str
    heading_number: int
    heading_name: str
    table_id: str
    table_name: str
    fields: list[tuple[str, list[Paragraph]]]
    filename: str


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as source:
        for chunk in iter(lambda: source.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def paragraph_text(paragraph: ET.Element) -> str:
    chunks: list[str] = []
    for node in paragraph.iter():
        if node.tag == W + "t":
            chunks.append(node.text or "")
        elif node.tag == W + "tab":
            chunks.append("\t")
        elif node.tag == W + "br":
            chunks.append("\n")
    return "".join(chunks).strip()


def cell_paragraphs(cell: ET.Element) -> list[Paragraph]:
    result: list[Paragraph] = []
    for paragraph in cell.iter(W + "p"):
        text = paragraph_text(paragraph)
        if not text:
            continue
        properties = paragraph.find(W + "pPr")
        numbered = properties is not None and properties.find(W + "numPr") is not None
        result.append(Paragraph(text=text, numbered=numbered))
    return result


def table_rows(table: ET.Element) -> list[list[list[Paragraph]]]:
    rows: list[list[list[Paragraph]]] = []
    for row in table.findall(W + "tr"):
        rows.append([cell_paragraphs(cell) for cell in row.findall(W + "tc")])
    return rows


def plain_cell(paragraphs: list[Paragraph]) -> str:
    return " / ".join(item.text for item in paragraphs)


def first_row_text(rows: list[list[list[Paragraph]]]) -> list[str]:
    if not rows:
        return []
    return [plain_cell(cell) for cell in rows[0]]


def slugify(value: str) -> str:
    normalized = unicodedata.normalize("NFKD", value)
    ascii_value = "".join(ch for ch in normalized if not unicodedata.combining(ch))
    ascii_value = ascii_value.replace("đ", "d").replace("Đ", "D")
    return re.sub(r"[^a-z0-9]+", "-", ascii_value.lower()).strip("-")


def escape_table(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", "<br>")


def render_paragraphs(paragraphs: list[Paragraph]) -> list[str]:
    if not paragraphs:
        return ["_Không có nội dung trong bảng nguồn._"]
    if len(paragraphs) == 1:
        return [paragraphs[0].text]

    rendered: list[str] = []
    for item in paragraphs:
        marker = "1." if item.numbered else "-"
        rendered.append(f"{marker} {item.text}")
    return rendered


def extract_heading_sections(body: ET.Element) -> list[tuple[str, str, int, str]]:
    sections: list[tuple[str, str, int, str]] = []
    pattern = re.compile(r"^(3\.\d+\.)\s+(UC-(\d+)):\s*(.+)$")
    in_use_cases = False
    for node in list(body):
        if node.tag != W + "p":
            continue
        text = paragraph_text(node)
        if text == "3. Phân tích các Use Case / Use cases analysis":
            in_use_cases = True
            continue
        if in_use_cases and text == "4. Môi trường hoạt động / Operating Environment":
            break
        if not in_use_cases:
            continue
        match = pattern.match(text)
        if match:
            sections.append(
                (match.group(1), match.group(2), int(match.group(3)), match.group(4))
            )
    return sections


def extract_source() -> tuple[str, list[tuple[str, str, str]], list[DetailSection]]:
    source_hash = sha256(SOURCE)
    if source_hash != EXPECTED_SOURCE_HASH:
        raise RuntimeError(
            "Source hash changed. Review the DOCX and update the converter before regenerating: "
            f"expected {EXPECTED_SOURCE_HASH}, got {source_hash}"
        )

    with ZipFile(SOURCE) as archive:
        root = ET.fromstring(archive.read("word/document.xml"))

    body = root.find(W + "body")
    if body is None:
        raise RuntimeError("DOCX document body is missing")

    parsed_tables = [(table, table_rows(table)) for table in root.iter(W + "tbl")]
    catalogue_tables = [
        rows
        for _, rows in parsed_tables
        if first_row_text(rows) == ["STT", "Mã UC", "Tên UC"]
    ]
    if len(catalogue_tables) != 1:
        raise RuntimeError(f"Expected one UC catalogue, found {len(catalogue_tables)}")

    catalogue: list[tuple[str, str, str]] = []
    for row in catalogue_tables[0][1:]:
        if len(row) < 3:
            continue
        catalogue.append(tuple(plain_cell(cell) for cell in row[:3]))
    if len(catalogue) != EXPECTED_CATALOGUE_ROWS:
        raise RuntimeError(
            f"Expected {EXPECTED_CATALOGUE_ROWS} catalogue rows, found {len(catalogue)}"
        )

    detail_rows = [
        rows
        for _, rows in parsed_tables
        if first_row_text(rows) == ["Nội dung", "Mô tả"]
        and any(
            len(row) >= 2 and plain_cell(row[0]) == "Use Case ID" for row in rows
        )
    ]
    headings = extract_heading_sections(body)
    if len(detail_rows) != EXPECTED_DETAIL_TABLES or len(headings) != EXPECTED_DETAIL_TABLES:
        raise RuntimeError(
            "Unexpected detailed UC count: "
            f"tables={len(detail_rows)}, headings={len(headings)}, "
            f"expected={EXPECTED_DETAIL_TABLES}"
        )

    details: list[DetailSection] = []
    for heading, rows in zip(headings, detail_rows, strict=True):
        section_number, heading_id, heading_number, heading_name = heading
        fields: list[tuple[str, list[Paragraph]]] = []
        for row in rows[1:]:
            if len(row) < 2:
                continue
            fields.append((plain_cell(row[0]), row[1]))
        field_map = {key: plain_cell(value) for key, value in fields}
        table_id = field_map.get("Use Case ID", "")
        table_name = field_map.get("Use Case Name", "")
        filename = f"UC-{heading_number:02d}-{slugify(heading_name)}.md"
        details.append(
            DetailSection(
                section_number=section_number,
                heading_id=heading_id,
                heading_number=heading_number,
                heading_name=heading_name,
                table_id=table_id,
                table_name=table_name,
                fields=fields,
                filename=filename,
            )
        )
    return source_hash, catalogue, details


def detail_consistency(detail: DetailSection) -> str:
    expected_id = f"UC-{detail.heading_number}"
    if detail.heading_id != expected_id:
        return f"Tiêu đề có ID `{detail.heading_id}`, không khớp vị trí `{expected_id}`."
    if detail.table_id != detail.heading_id:
        return f"Tiêu đề `{detail.heading_id}` nhưng bảng ghi `{detail.table_id}`."
    if detail.table_name != detail.heading_name:
        return (
            f"Tên trong tiêu đề “{detail.heading_name}” khác tên trong bảng "
            f"“{detail.table_name}”."
        )
    return "Khớp giữa tiêu đề và bảng đặc tả."


def render_detail(detail: DetailSection, source_hash: str) -> str:
    lines = [
        f"# {detail.heading_id}: {detail.heading_name}",
        "",
        "> Loại tài liệu: **SRS baseline chuyển đổi nguyên trạng**; không tự động đồng nghĩa với requirement đã được PO phê duyệt để triển khai.",
        f"> Nguồn: `SRS/SRS (SmartTrọ).docx`, mục `{detail.section_number}`; SHA-256 `{source_hash}`.",
        f"> Đồng bộ: {CONVERSION_DATE}.",
        "",
    ]

    consistency = detail_consistency(detail)
    if consistency != "Khớp giữa tiêu đề và bảng đặc tả.":
        lines.extend(
            [
                "## Cảnh báo truy vết nguồn",
                "",
                f"> **Không tự sửa số hoặc nội dung:** {consistency}",
                "",
            ]
        )

    lines.extend(["## Đặc tả use case", ""])
    for key, value in detail.fields:
        lines.extend([f"### {key}", "", *render_paragraphs(value), ""])

    lines.extend(
        [
            "## Activity Diagram",
            "",
            "> DOCX nguồn có tiêu đề “Activity Diagram” cho mục này nhưng không có nội dung sơ đồ nhúng ngay trong phần tương ứng. Không tạo sơ đồ giả định trong baseline.",
            "",
        ]
    )

    approved_doc = APPROVED_IMPLEMENTATION_DOCS.get(detail.heading_number)
    if approved_doc:
        lines.extend(
            [
                "## Tài liệu triển khai đã được phê duyệt",
                "",
                f"- [Living implementation specification]({approved_doc})",
                "- Khi baseline và living spec khác nhau, PM/Dev/QA dùng living spec đã phê duyệt cho implementation và ghi rõ deviation khỏi SRS nguồn.",
                "",
            ]
        )
    return "\n".join(lines).rstrip() + "\n"


def source_issue_notes() -> list[str]:
    return [
        "Catalogue có `UC-6 — Tạo mới chữ ký điện tử` và `UC-7 — Cập nhật chữ ký điện tử`, nhưng phần phân tích chi tiết không có hai UC này.",
        "Từ chức năng Đổi mật khẩu tới Thống kê chi phí theo tháng, số UC trong catalogue và phần phân tích chi tiết lệch nhau hai đơn vị; không được tự động coi hai ID là tương đương.",
        "Mục chi tiết cuối có tiêu đề `UC-31: Báo cáo chi tiêu`, nhưng bảng bên trong ghi `Use Case ID = UC-32`; catalogue lại ghi `UC-33 — Báo cáo chi tiết`.",
        "Catalogue có 33 UC nhưng DOCX chỉ có 31 bảng đặc tả chi tiết. Các khoảng trống này phải được PO/BA sửa ở nguồn trước khi dùng làm requirement triển khai.",
    ]


def render_readme(
    source_hash: str,
    catalogue: list[tuple[str, str, str]],
    details: list[DetailSection],
) -> str:
    lines = [
        "# SmartTrọ SRS Use Case Baseline",
        "",
        f"> Chuyển đổi ngày {CONVERSION_DATE} từ `SRS/SRS (SmartTrọ).docx`.",
        f"> SHA-256 nguồn: `{source_hash}`.",
        "",
        "Thư mục này là bản đối chiếu đầy đủ những gì **đang tồn tại trong SRS DOCX**. Nó khác với `docs/use-cases/smarttro/`, nơi chứa living spec đã được PO chốt và dùng để triển khai code.",
        "",
        "## Phạm vi chuyển đổi",
        "",
        f"- Danh mục nguồn: **{len(catalogue)} UC**.",
        f"- Bảng đặc tả chi tiết thực tế trong DOCX: **{len(details)} UC**.",
        "- Mỗi bảng đặc tả được xuất thành một file riêng để agent có thể đọc ổn định và truy vết về đúng mục trong SRS.",
        "- Nội dung không được tự suy diễn để lấp các UC thiếu hoặc sửa lệch số trong file nguồn.",
        "",
        "## Các bất nhất cần PO/BA xử lý ở SRS nguồn",
        "",
    ]
    lines.extend(f"- {note}" for note in source_issue_notes())

    lines.extend(
        [
            "",
            "## Danh mục UC trong SRS nguồn",
            "",
            "| STT | Mã UC | Tên UC |",
            "| ---: | --- | --- |",
        ]
    )
    for stt, uc_id, name in catalogue:
        lines.append(f"| {escape_table(stt)} | {escape_table(uc_id)} | {escape_table(name)} |")

    lines.extend(
        [
            "",
            "## Phân tích chi tiết thực tế trong SRS nguồn",
            "",
            "| Mục SRS | Tiêu đề mục | ID trong bảng | Tên trong bảng | Baseline | Đối chiếu |",
            "| --- | --- | --- | --- | --- | --- |",
        ]
    )
    for detail in details:
        consistency = detail_consistency(detail)
        lines.append(
            "| "
            + " | ".join(
                [
                    escape_table(detail.section_number),
                    escape_table(f"{detail.heading_id}: {detail.heading_name}"),
                    escape_table(detail.table_id),
                    escape_table(detail.table_name),
                    f"[`{detail.filename}`]({detail.filename})",
                    escape_table(consistency),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## Quan hệ với tài liệu triển khai",
            "",
            "- UC-01, UC-02 và UC-03 đã có living spec được PO phê duyệt trong [`docs/use-cases/smarttro/`](../../../docs/use-cases/smarttro/README.md); giữ nguyên các file đó.",
            "- Hai UC chữ ký điện tử không có bảng đặc tả trong DOCX nguồn, nhưng đã có Activity Diagram. Vì vậy chúng được soạn thành **living spec Draft bổ sung**, không được coi là nội dung trích xuất từ DOCX:",
            *[
                f"  - {uc_id} — {name}: [`{Path(path).name}`]({path})"
                for uc_id, name, path in SUPPLEMENTAL_ACTIVITY_DIAGRAM_DOCS
            ],
            "- Khi chuẩn bị UC mới, PM phải bắt đầu từ baseline tương ứng tại đây, sau đó ghi rõ quyết định PO, deviation, UI, API, test scope và gate triển khai trong living spec riêng.",
            "- Không dùng việc “chưa tạo living spec” để kết luận SRS không có UC; baseline của toàn bộ SRS phải luôn được tạo trước và độc lập với tiến độ coding.",
            "",
        ]
    )
    return "\n".join(lines)


def render_main_section(
    catalogue: list[tuple[str, str, str]], details: list[DetailSection]
) -> str:
    lines = [
        SECTION_START,
        "",
        f"> Khôi phục ngày {CONVERSION_DATE} từ các bảng lồng trong DOCX nguồn. Danh mục có {len(catalogue)} UC; phần đặc tả chi tiết có {len(details)} bảng và được tách sang [`use-cases/`](use-cases/README.md).",
        "> Ba living spec UC-01 đến UC-03 trong `docs/use-cases/smarttro/` được giữ nguyên vì đã dùng để triển khai code.",
        "",
        "### 3.1. Danh sách các use case",
        "",
        "| STT | Mã UC | Tên UC |",
        "| ---: | --- | --- |",
    ]
    for stt, uc_id, name in catalogue:
        lines.append(f"| {escape_table(stt)} | {escape_table(uc_id)} | {escape_table(name)} |")

    lines.extend(
        [
            "",
            "### Tài liệu bổ sung từ Activity Diagram (Draft)",
            "",
            "> DOCX nguồn chỉ liệt kê hai UC chữ ký điện tử trong catalogue và không có bảng đặc tả tương ứng. Các tài liệu dưới đây được soạn từ Activity Diagram hiện có, là living spec Draft và không phải nội dung trích xuất từ DOCX.",
            "",
        ]
    )
    for uc_id, name, path in SUPPLEMENTAL_ACTIVITY_DIAGRAM_DOCS:
        main_relative = path.replace("../../../", "../../")
        lines.append(f"- [{uc_id} — {name}]({main_relative})")

    lines.extend(["", "### 3.2–3.32. Đặc tả chi tiết", ""])
    for detail in details:
        lines.extend(
            [
                f"#### {detail.section_number} {detail.heading_id}: {detail.heading_name}",
                "",
                f"- [Bản baseline chuyển đổi đầy đủ](use-cases/{detail.filename})",
            ]
        )
        approved_doc = APPROVED_IMPLEMENTATION_DOCS.get(detail.heading_number)
        if approved_doc:
            main_relative = approved_doc.replace("../../../", "../../")
            lines.append(f"- [Living implementation specification đã phê duyệt]({main_relative})")
        consistency = detail_consistency(detail)
        if consistency != "Khớp giữa tiêu đề và bảng đặc tả.":
            lines.append(f"- **Cảnh báo nguồn:** {consistency}")
        lines.append("")

    lines.extend(
        [
            "### 3.33. Ghi chú đối chiếu nguồn",
            "",
            *[f"- {note}" for note in source_issue_notes()],
            "",
        ]
    )
    return "\n".join(lines).rstrip()


def update_main_mirror(section: str) -> None:
    text = MAIN_MIRROR.read_text(encoding="utf-8")
    start = text.find(SECTION_START)
    end = text.find(SECTION_END, start)
    if start < 0 or end < 0:
        raise RuntimeError("Could not locate the use-case section boundaries in the SRS mirror")
    replacement = section + "\n\n"
    MAIN_MIRROR.write_text(text[:start] + replacement + text[end:], encoding="utf-8")


def main() -> None:
    source_hash, catalogue, details = extract_source()
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    for stale in OUTPUT_DIR.glob("UC-*.md"):
        stale.unlink()
    for detail in details:
        (OUTPUT_DIR / detail.filename).write_text(
            render_detail(detail, source_hash), encoding="utf-8"
        )

    (OUTPUT_DIR / "README.md").write_text(
        render_readme(source_hash, catalogue, details), encoding="utf-8"
    )
    update_main_mirror(render_main_section(catalogue, details))

    print(f"source_sha256={source_hash}")
    print(f"catalogue_rows={len(catalogue)}")
    print(f"detail_files={len(details)}")
    print(f"output={OUTPUT_DIR}")


if __name__ == "__main__":
    main()
