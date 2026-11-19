#!/usr/bin/env python3
"""Reconcile legacy Smart Platform Draw.io auth pages with the email flows."""

from __future__ import annotations

import argparse
import xml.etree.ElementTree as ET
from pathlib import Path


PAGE_SIGN_UP_PHONE = "AD_Sign Up (By Phone)"
PAGE_SIGN_UP_EMAIL = "AD_Sign Up (By Email)"
PAGE_SIGN_IN_PHONE = "AD_Sign In (By Phone)"
PAGE_SIGN_IN_EMAIL = "AD_Sign In (By Email)"


APP_CONFIG = {
    "smarttro": {
        "actor": "Renter",
        "app": "SmartTrọ",
        "signup": {
            "container": "Ke1mENM3ikKIdnPlOIF_-2",
            "actor_lane": "Ke1mENM3ikKIdnPlOIF_-3",
            "system_lane": "Ke1mENM3ikKIdnPlOIF_-44",
            "start": "Ke1mENM3ikKIdnPlOIF_-5",
            "open": "Ke1mENM3ikKIdnPlOIF_-7",
            "sign_in_screen": "8eRr943gss0spf7AQDu7-0",
            "sign_up_link": "8eRr943gss0spf7AQDu7-2",
            "sign_up_screen": "8eRr943gss0spf7AQDu7-4",
            "email_input": "8eRr943gss0spf7AQDu7-6",
            "send_otp_click": "8eRr943gss0spf7AQDu7-8",
            "email_check": "aJ25MjYCsSjSJg_o7QVp-0",
            "send_otp": "8eRr943gss0spf7AQDu7-14",
            "otp_screen": "8eRr943gss0spf7AQDu7-22",
            "otp_input": "8eRr943gss0spf7AQDu7-10",
            "otp_continue": "8eRr943gss0spf7AQDu7-12",
            "otp_verify": "8eRr943gss0spf7AQDu7-18",
            "otp_decision": "62G0FJVdS8SaGgNECkPI-0",
            "otp_error": "62G0FJVdS8SaGgNECkPI-1",
            "personal_screen": "62G0FJVdS8SaGgNECkPI-4",
            "password_input": "62G0FJVdS8SaGgNECkPI-11",
            "register_click": "62G0FJVdS8SaGgNECkPI-13",
            "save_account": "62G0FJVdS8SaGgNECkPI-18",
            "return_sign_in": "62G0FJVdS8SaGgNECkPI-19",
            "end": "Ke1mENM3ikKIdnPlOIF_-43",
            "remove": [
                "62G0FJVdS8SaGgNECkPI-8",
                "62G0FJVdS8SaGgNECkPI-17",
                "62G0FJVdS8SaGgNECkPI-22",
            ],
        },
        "signin": {
            "container": "MzLh7MvPFJbDZgQiAAbO-2",
            "actor_lane": "MzLh7MvPFJbDZgQiAAbO-3",
            "system_lane": "MzLh7MvPFJbDZgQiAAbO-17",
            "start": "MzLh7MvPFJbDZgQiAAbO-5",
            "open": "MzLh7MvPFJbDZgQiAAbO-6",
            "screen": "MzLh7MvPFJbDZgQiAAbO-18",
            "credential_input": "MzLh7MvPFJbDZgQiAAbO-9",
            "submit": "MzLh7MvPFJbDZgQiAAbO-10",
            "validate": "MzLh7MvPFJbDZgQiAAbO-46",
            "decision": "MzLh7MvPFJbDZgQiAAbO-29",
            "error": "MzLh7MvPFJbDZgQiAAbO-31",
            "save_session": "MzLh7MvPFJbDZgQiAAbO-33",
            "home": "PaoyaXu5cLkNTDpQ1k4e-0",
            "end": "MzLh7MvPFJbDZgQiAAbO-44",
            "remove": [
                "MzLh7MvPFJbDZgQiAAbO-11",
                "MzLh7MvPFJbDZgQiAAbO-12",
                "MzLh7MvPFJbDZgQiAAbO-21",
                "MzLh7MvPFJbDZgQiAAbO-22",
                "MzLh7MvPFJbDZgQiAAbO-23",
                "MzLh7MvPFJbDZgQiAAbO-34",
            ],
        },
        "signout": {
            "container": "ijAeuzC8Iia17ykZBsW7-2",
            "actor_lane": "ijAeuzC8Iia17ykZBsW7-3",
            "system_lane": "ijAeuzC8Iia17ykZBsW7-13",
            "start": "ijAeuzC8Iia17ykZBsW7-5",
            "open": "ijAeuzC8Iia17ykZBsW7-6",
            "home": "cjnTIpnNan7ArjKUCE9Z-9",
            "menu_click": "cjnTIpnNan7ArjKUCE9Z-11",
            "menu_screen": "ijAeuzC8Iia17ykZBsW7-18",
            "signout_click": "cjnTIpnNan7ArjKUCE9Z-13",
            "revoke": "ijAeuzC8Iia17ykZBsW7-26",
            "sign_in_screen": "ijAeuzC8Iia17ykZBsW7-35",
            "end": "ijAeuzC8Iia17ykZBsW7-31",
            "remove": [
                "cjnTIpnNan7ArjKUCE9Z-0",
                "cjnTIpnNan7ArjKUCE9Z-3",
                "cjnTIpnNan7ArjKUCE9Z-7",
            ],
        },
        "forgot": {
            "container": "U9-Ry4HMBeFa4APZCm0K-2",
            "actor_lane": "U9-Ry4HMBeFa4APZCm0K-3",
            "system_lane": "U9-Ry4HMBeFa4APZCm0K-18",
            "start": "U9-Ry4HMBeFa4APZCm0K-5",
            "open": "U9-Ry4HMBeFa4APZCm0K-6",
            "sign_in_screen": "U9-Ry4HMBeFa4APZCm0K-10",
            "forgot_link": "Xek2mY_xYS014ffLprHc-0",
            "forgot_screen": "Xek2mY_xYS014ffLprHc-2",
            "email_input": "Xek2mY_xYS014ffLprHc-4",
            "email_check": "U9-Ry4HMBeFa4APZCm0K-25",
            "eligibility": "I-irvnMbw9T40XeqaJsz-0",
            "no_send": "I-irvnMbw9T40XeqaJsz-4",
            "send_otp": "c3eX8QOnYDbT1643O61G-2",
            "join": "c3eX8QOnYDbT1643O61G-1",
            "otp_screen": "c3eX8QOnYDbT1643O61G-3",
            "otp_input": "c3eX8QOnYDbT1643O61G-8",
            "otp_submit": "U9-Ry4HMBeFa4APZCm0K-16",
            "otp_verify": "c3eX8QOnYDbT1643O61G-11",
            "otp_decision": "c3eX8QOnYDbT1643O61G-12",
            "password_screen": "c3eX8QOnYDbT1643O61G-18",
            "otp_error": "c3eX8QOnYDbT1643O61G-21",
            "password_input": "c3eX8QOnYDbT1643O61G-26",
            "password_submit": "c3eX8QOnYDbT1643O61G-28",
            "password_check": "c3eX8QOnYDbT1643O61G-30",
            "save_password": "c3eX8QOnYDbT1643O61G-31",
            "return_sign_in": "c3eX8QOnYDbT1643O61G-32",
            "end": "U9-Ry4HMBeFa4APZCm0K-22",
            "remove": ["c3eX8QOnYDbT1643O61G-0", "c3eX8QOnYDbT1643O61G-1"],
        },
    },
    "smartchu": {
        "actor": "Owner",
        "app": "SmartChủ",
        "signup": {
            "container": "PuV6NnfnilUMN9S_Ymnt-0",
            "actor_lane": "PuV6NnfnilUMN9S_Ymnt-1",
            "system_lane": "PuV6NnfnilUMN9S_Ymnt-15",
            "start": "PuV6NnfnilUMN9S_Ymnt-3",
            "open": "PuV6NnfnilUMN9S_Ymnt-4",
            "sign_in_screen": "PuV6NnfnilUMN9S_Ymnt-16",
            "sign_up_link": "PuV6NnfnilUMN9S_Ymnt-5",
            "sign_up_screen": "PuV6NnfnilUMN9S_Ymnt-17",
            "email_input": "PuV6NnfnilUMN9S_Ymnt-7",
            "send_otp_click": "PuV6NnfnilUMN9S_Ymnt-8",
            "email_check": "PuV6NnfnilUMN9S_Ymnt-44",
            "send_otp": "PuV6NnfnilUMN9S_Ymnt-19",
            "otp_screen": "PuV6NnfnilUMN9S_Ymnt-20",
            "otp_input": "PuV6NnfnilUMN9S_Ymnt-10",
            "otp_continue": "PuV6NnfnilUMN9S_Ymnt-9",
            "otp_verify": "PuV6NnfnilUMN9S_Ymnt-21",
            "otp_decision": "PuV6NnfnilUMN9S_Ymnt-27",
            "otp_error": "PuV6NnfnilUMN9S_Ymnt-29",
            "personal_screen": "PuV6NnfnilUMN9S_Ymnt-31",
            "password_input": "PuV6NnfnilUMN9S_Ymnt-13",
            "register_click": "PuV6NnfnilUMN9S_Ymnt-14",
            "save_account": "PuV6NnfnilUMN9S_Ymnt-36",
            "return_sign_in": "PuV6NnfnilUMN9S_Ymnt-39",
            "end": "PuV6NnfnilUMN9S_Ymnt-42",
            "remove": [
                "PuV6NnfnilUMN9S_Ymnt-32",
                "PuV6NnfnilUMN9S_Ymnt-33",
                "PuV6NnfnilUMN9S_Ymnt-40",
            ],
        },
        "signin": {
            "container": "llL8XYXRJV3uZxQj6A8Z-40",
            "actor_lane": "llL8XYXRJV3uZxQj6A8Z-41",
            "system_lane": "llL8XYXRJV3uZxQj6A8Z-51",
            "start": "llL8XYXRJV3uZxQj6A8Z-43",
            "open": "llL8XYXRJV3uZxQj6A8Z-44",
            "screen": "llL8XYXRJV3uZxQj6A8Z-52",
            "credential_input": "llL8XYXRJV3uZxQj6A8Z-46",
            "submit": "llL8XYXRJV3uZxQj6A8Z-47",
            "validate": "llL8XYXRJV3uZxQj6A8Z-71",
            "decision": "llL8XYXRJV3uZxQj6A8Z-62",
            "error": "llL8XYXRJV3uZxQj6A8Z-64",
            "save_session": "llL8XYXRJV3uZxQj6A8Z-66",
            "home": "llL8XYXRJV3uZxQj6A8Z-73",
            "end": "llL8XYXRJV3uZxQj6A8Z-69",
            "remove": [
                "llL8XYXRJV3uZxQj6A8Z-48",
                "llL8XYXRJV3uZxQj6A8Z-49",
                "llL8XYXRJV3uZxQj6A8Z-54",
                "llL8XYXRJV3uZxQj6A8Z-55",
                "llL8XYXRJV3uZxQj6A8Z-56",
                "llL8XYXRJV3uZxQj6A8Z-68",
            ],
        },
        "signout": {
            "container": "8YSoJiMQPqwq8XEEb7fi-0",
            "actor_lane": "8YSoJiMQPqwq8XEEb7fi-1",
            "system_lane": "8YSoJiMQPqwq8XEEb7fi-16",
            "start": "8YSoJiMQPqwq8XEEb7fi-3",
            "open": "8YSoJiMQPqwq8XEEb7fi-4",
            "home": "8YSoJiMQPqwq8XEEb7fi-23",
            "menu_click": "8YSoJiMQPqwq8XEEb7fi-14",
            "menu_screen": "8YSoJiMQPqwq8XEEb7fi-17",
            "signout_click": "8YSoJiMQPqwq8XEEb7fi-15",
            "revoke": "8YSoJiMQPqwq8XEEb7fi-19",
            "sign_in_screen": "8YSoJiMQPqwq8XEEb7fi-22",
            "end": "8YSoJiMQPqwq8XEEb7fi-20",
            "remove": [
                "8YSoJiMQPqwq8XEEb7fi-5",
                "8YSoJiMQPqwq8XEEb7fi-8",
                "8YSoJiMQPqwq8XEEb7fi-12",
            ],
        },
        "forgot": {
            "container": "OKeWYJX48u6LaeIK9Js--0",
            "actor_lane": "OKeWYJX48u6LaeIK9Js--1",
            "system_lane": "OKeWYJX48u6LaeIK9Js--13",
            "start": "OKeWYJX48u6LaeIK9Js--3",
            "open": "OKeWYJX48u6LaeIK9Js--4",
            "sign_in_screen": "OKeWYJX48u6LaeIK9Js--17",
            "forgot_link": "OKeWYJX48u6LaeIK9Js--6",
            "forgot_screen": "OKeWYJX48u6LaeIK9Js--18",
            "email_input": "OKeWYJX48u6LaeIK9Js--7",
            "email_check": "OKeWYJX48u6LaeIK9Js--16",
            "eligibility": "OKeWYJX48u6LaeIK9Js--23",
            "no_send": "OKeWYJX48u6LaeIK9Js--25",
            "send_otp": "OKeWYJX48u6LaeIK9Js--31",
            "join": "OKeWYJX48u6LaeIK9Js--29",
            "otp_screen": "OKeWYJX48u6LaeIK9Js--33",
            "otp_input": "OKeWYJX48u6LaeIK9Js--9",
            "otp_submit": "OKeWYJX48u6LaeIK9Js--5",
            "otp_verify": "OKeWYJX48u6LaeIK9Js--35",
            "otp_decision": "OKeWYJX48u6LaeIK9Js--40",
            "password_screen": "OKeWYJX48u6LaeIK9Js--41",
            "otp_error": "OKeWYJX48u6LaeIK9Js--42",
            "password_input": "OKeWYJX48u6LaeIK9Js--11",
            "password_submit": "OKeWYJX48u6LaeIK9Js--12",
            "password_check": "OKeWYJX48u6LaeIK9Js--44",
            "save_password": "OKeWYJX48u6LaeIK9Js--46",
            "return_sign_in": "OKeWYJX48u6LaeIK9Js--48",
            "end": "OKeWYJX48u6LaeIK9Js--14",
            "remove": ["OKeWYJX48u6LaeIK9Js--28", "OKeWYJX48u6LaeIK9Js--29"],
        },
    },
}


def geometry(cell: ET.Element) -> ET.Element:
    found = cell.find("mxGeometry")
    if found is None:
        found = ET.SubElement(cell, "mxGeometry", {"as": "geometry"})
    return found


def set_box(cell: ET.Element, x: int, y: int, width: int, height: int) -> None:
    geo = geometry(cell)
    geo.attrib.update(
        {"x": str(x), "y": str(y), "width": str(width), "height": str(height)}
    )


def index_cells(page: ET.Element) -> dict[str, ET.Element]:
    return {cell.get("id"): cell for cell in page.findall(".//mxCell") if cell.get("id")}


def remove_cells(root: ET.Element, ids: set[str]) -> None:
    expanded = set(ids)
    changed = True
    while changed:
        changed = False
        for cell in root.findall("mxCell"):
            if cell.get("parent") in expanded and cell.get("id") not in expanded:
                expanded.add(cell.get("id"))
                changed = True
    for cell in list(root.findall("mxCell")):
        if cell.get("id") in expanded:
            root.remove(cell)


def clear_edges(root: ET.Element) -> None:
    edge_ids = {cell.get("id") for cell in root.findall("mxCell") if cell.get("edge") == "1"}
    remove_cells(root, edge_ids)


def add_vertex(
    root: ET.Element,
    *,
    cell_id: str,
    parent: str,
    value: str,
    style: str,
    x: int,
    y: int,
    width: int = 120,
    height: int = 60,
) -> ET.Element:
    cell = ET.SubElement(
        root,
        "mxCell",
        {"id": cell_id, "value": value, "style": style, "vertex": "1", "parent": parent},
    )
    ET.SubElement(
        cell,
        "mxGeometry",
        {
            "x": str(x),
            "y": str(y),
            "width": str(width),
            "height": str(height),
            "as": "geometry",
        },
    )
    return cell


def add_edge(
    root: ET.Element,
    *,
    cell_id: str,
    parent: str,
    source: str,
    target: str,
    style: str,
    label: str | None = None,
    label_style: str | None = None,
    label_x: float = -0.2,
    label_offset_x: float | None = None,
    label_offset_y: float = 0,
) -> None:
    cells = {cell.get("id"): cell for cell in root.findall("mxCell") if cell.get("id")}
    source_cell = cells.get(source)
    target_cell = cells.get(target)
    if source_cell is not None and target_cell is not None:
        source_parent = cells.get(source_cell.get("parent"))
        target_parent = cells.get(target_cell.get("parent"))
        if (
            source_parent is not None
            and target_parent is not None
            and source_parent is not target_parent
            and "swimlane" in source_parent.get("style", "")
            and "swimlane" in target_parent.get("style", "")
        ):
            source_x = float(geometry(source_parent).get("x", "0") or 0)
            target_x = float(geometry(target_parent).get("x", "0") or 0)
            if source_x < target_x:
                style += "exitX=1;exitY=0.5;entryX=0;entryY=0.5;"
            else:
                style += "exitX=0;exitY=0.5;entryX=1;entryY=0.5;"
    edge = ET.SubElement(
        root,
        "mxCell",
        {
            "id": cell_id,
            "style": style,
            "edge": "1",
            "parent": parent,
            "source": source,
            "target": target,
        },
    )
    ET.SubElement(edge, "mxGeometry", {"relative": "1", "as": "geometry"})
    if label:
        label_cell = ET.SubElement(
            root,
            "mxCell",
            {
                "id": f"{cell_id}-label",
                "value": label,
                "style": label_style
                or "edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];fontSize=12;",
                "connectable": "0",
                "vertex": "1",
                "parent": cell_id,
            },
        )
        label_geometry = ET.SubElement(
            label_cell,
            "mxGeometry",
            {"x": str(label_x), "relative": "1", "as": "geometry"},
        )
        if label_offset_x is not None:
            ET.SubElement(
                label_geometry,
                "mxPoint",
                {"x": str(label_offset_x), "y": str(label_offset_y), "as": "offset"},
            )


def page_root(page: ET.Element) -> tuple[ET.Element, ET.Element]:
    model = page.find("mxGraphModel")
    if model is None:
        raise ValueError(f"Page {page.get('name')} has no mxGraphModel")
    root = model.find("root")
    if root is None:
        raise ValueError(f"Page {page.get('name')} has no root")
    return model, root


def get_page(document: ET.Element, *names: str) -> ET.Element:
    for name in names:
        for page in document.findall("diagram"):
            if page.get("name") == name:
                return page
    raise ValueError(f"Missing Draw.io page: {' or '.join(names)}")


def normalize_auth_page(page: ET.Element) -> None:
    """Give legacy two-lane auth diagrams enough width for the approved copy."""
    model, root = page_root(page)
    cells = index_cells(page)
    swimlanes = [
        cell
        for cell in root.findall("mxCell")
        if "swimlane" in cell.get("style", "")
    ]
    container = next(
        (
            cell
            for cell in swimlanes
            if sum(1 for lane in swimlanes if lane.get("parent") == cell.get("id")) >= 2
        ),
        None,
    )
    if container is None:
        return
    lanes = [cell for cell in swimlanes if cell.get("parent") == container.get("id")]
    if len(lanes) < 2:
        return
    lanes.sort(key=lambda lane: float(geometry(lane).get("x", "0")))
    actor_lane, system_lane = lanes[:2]

    model.set("pageWidth", "1100")
    container_geo = geometry(container)
    container_geo.attrib.update({"x": "0", "y": "0", "width": "1000"})
    geometry(actor_lane).attrib.update({"x": "0", "width": "500"})
    geometry(system_lane).attrib.update({"x": "500", "width": "500"})

    for cell in root.findall("mxCell"):
        if cell.get("vertex") != "1" or cell.get("parent") not in {
            actor_lane.get("id"),
            system_lane.get("id"),
        }:
            continue
        geo = geometry(cell)
        width = float(geo.get("width", "0") or 0)
        height = float(geo.get("height", "0") or 0)
        x = float(geo.get("x", "0") or 0)
        style = cell.get("style", "")

        if "rhombus" in style:
            decision_x = "320" if x >= 250 else "180"
            geo.attrib.update({"x": decision_x, "width": "140", "height": "80"})
        elif height <= 12 or "shape=line" in style:
            geo.attrib.update({"x": "100", "width": "300"})
        elif width <= 32:
            geo.attrib.update({"x": "235", "width": "30", "height": "30"})
        elif width <= 45:
            geo.attrib.update({"x": "230", "width": "40", "height": "40"})
        elif cell.get("parent") == actor_lane.get("id"):
            geo.attrib.update({"x": "140", "width": "220", "height": "80"})
        elif x <= 100:
            geo.attrib.update({"x": "30", "width": "200", "height": "80"})
        elif x >= 230:
            geo.attrib.update({"x": "270", "width": "200", "height": "80"})
        else:
            geo.attrib.update({"x": "140", "width": "220", "height": "80"})


def reconcile_signup(document: ET.Element, config: dict) -> None:
    page = get_page(document, PAGE_SIGN_UP_PHONE, PAGE_SIGN_UP_EMAIL)
    page.set("name", PAGE_SIGN_UP_EMAIL)
    model, root = page_root(page)
    cells = index_cells(page)
    ids = config["signup"]

    edge_style = "edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;"
    action_style = cells[ids["email_input"]].get("style", "")
    decision_style = cells[ids["otp_decision"]].get("style", "")

    clear_edges(root)
    remove_cells(root, set(ids["remove"]))
    cells = index_cells(page)

    model.set("pageHeight", "2300")
    cells[ids["container"]].set("value", "Đăng ký bằng email")
    geometry(cells[ids["container"]]).set("height", "2140")
    geometry(cells[ids["actor_lane"]]).set("height", "2120")
    geometry(cells[ids["system_lane"]]).set("height", "2120")
    cells[ids["actor_lane"]].set("value", config["actor"])

    values = {
        "open": f"Mở app {config['app']}",
        "email_input": "Nhập email",
        "send_otp_click": "Bấm nút Gửi OTP",
        "email_check": "Chuẩn hóa email; kiểm tra định dạng, unique và rate limit",
        "send_otp": "Gửi OTP 6 chữ số tới email vừa nhập",
        "otp_screen": "Hiển thị màn hình nhập OTP",
        "otp_input": "Nhập mã OTP nhận qua email",
        "otp_continue": "Bấm nút Tiếp tục",
        "otp_verify": "Xác thực OTP vừa nhập",
        "otp_decision": "OTP hợp lệ?",
        "otp_error": "Hiển thị lỗi OTP sai, hết hạn hoặc vượt số lần thử",
        "personal_screen": "Hiển thị màn hình Thông tin cá nhân",
        "password_input": "Nhập mật khẩu và xác nhận mật khẩu",
        "register_click": "Bấm nút Đăng ký",
        "save_account": "Tạo tài khoản với email đã xác minh",
        "return_sign_in": "Thông báo thành công; về Đăng nhập với email điền sẵn, không auto-login",
    }
    for key, value in values.items():
        cells[ids[key]].set("value", value)

    positions = {
        "start": (190, 60, 40, 40),
        "open": (150, 140, 120, 60),
        "sign_in_screen": (150, 140, 120, 60),
        "sign_up_link": (150, 260, 120, 60),
        "sign_up_screen": (150, 360, 120, 60),
        "email_input": (150, 460, 120, 60),
        "send_otp_click": (150, 580, 120, 60),
        "email_check": (150, 580, 120, 60),
        "send_otp": (60, 820, 120, 60),
        "otp_screen": (60, 920, 120, 60),
        "otp_input": (150, 920, 120, 60),
        "otp_continue": (150, 1020, 120, 60),
        "otp_verify": (150, 1020, 120, 60),
        "otp_decision": (190, 1120, 40, 40),
        "otp_error": (40, 1220, 120, 60),
        "personal_screen": (260, 1220, 120, 60),
        "password_input": (150, 1580, 120, 60),
        "register_click": (150, 1700, 120, 60),
        "save_account": (150, 1820, 120, 60),
        "return_sign_in": (150, 1940, 120, 60),
        "end": (195, 2060, 30, 30),
    }
    for key, box in positions.items():
        set_box(cells[ids[key]], *box)

    email_decision = add_vertex(
        root,
        cell_id="auth-email-acceptable",
        parent=ids["system_lane"],
        value="Có thể tiếp tục?",
        style=decision_style,
        x=190,
        y=700,
        width=40,
        height=40,
    )
    email_rejected = add_vertex(
        root,
        cell_id="auth-email-rejected",
        parent=ids["system_lane"],
        value="Không tạo tài khoản trùng; hiển thị hướng dẫn phù hợp",
        style=action_style,
        x=260,
        y=820,
    )
    personal_input = add_vertex(
        root,
        cell_id="auth-personal-input",
        parent=ids["actor_lane"],
        value="Nhập tên hiển thị (bắt buộc) và SĐT liên hệ (không bắt buộc, không unique)",
        style=action_style,
        x=150,
        y=1340,
    )
    personal_continue = add_vertex(
        root,
        cell_id="auth-personal-continue",
        parent=ids["actor_lane"],
        value="Bấm nút Tiếp tục",
        style=action_style,
        x=150,
        y=1460,
    )
    personal_validate = add_vertex(
        root,
        cell_id="auth-personal-validate",
        parent=ids["system_lane"],
        value="Kiểm tra thông tin cá nhân",
        style=action_style,
        x=60,
        y=1460,
    )
    password_screen = add_vertex(
        root,
        cell_id="auth-password-screen",
        parent=ids["system_lane"],
        value="Hiển thị màn hình tạo mật khẩu",
        style=action_style,
        x=260,
        y=1580,
    )

    chain = [
        (ids["start"], ids["open"]),
        (ids["open"], ids["sign_in_screen"]),
        (ids["sign_in_screen"], ids["sign_up_link"]),
        (ids["sign_up_link"], ids["sign_up_screen"]),
        (ids["sign_up_screen"], ids["email_input"]),
        (ids["email_input"], ids["send_otp_click"]),
        (ids["send_otp_click"], ids["email_check"]),
        (ids["email_check"], email_decision.get("id")),
    ]
    for number, (source, target) in enumerate(chain, 1):
        add_edge(
            root,
            cell_id=f"auth-signup-chain-{number}",
            parent=ids["container"],
            source=source,
            target=target,
            style=edge_style,
        )
    add_edge(
        root,
        cell_id="auth-signup-email-ok",
        parent=ids["system_lane"],
        source=email_decision.get("id"),
        target=ids["send_otp"],
        style=edge_style,
        label="Có",
    )
    add_edge(
        root,
        cell_id="auth-signup-email-rejected",
        parent=ids["system_lane"],
        source=email_decision.get("id"),
        target=email_rejected.get("id"),
        style=edge_style,
        label="Không",
    )
    add_edge(
        root,
        cell_id="auth-signup-email-retry",
        parent=ids["container"],
        source=email_rejected.get("id"),
        target=ids["email_input"],
        style=edge_style,
    )
    for number, (source, target) in enumerate(
        [
            (ids["send_otp"], ids["otp_screen"]),
            (ids["otp_screen"], ids["otp_input"]),
            (ids["otp_input"], ids["otp_continue"]),
            (ids["otp_continue"], ids["otp_verify"]),
            (ids["otp_verify"], ids["otp_decision"]),
        ],
        1,
    ):
        add_edge(
            root,
            cell_id=f"auth-signup-otp-{number}",
            parent=ids["container"],
            source=source,
            target=target,
            style=edge_style,
        )
    add_edge(
        root,
        cell_id="auth-signup-otp-invalid",
        parent=ids["system_lane"],
        source=ids["otp_decision"],
        target=ids["otp_error"],
        style=edge_style,
        label="Không hợp lệ",
    )
    add_edge(
        root,
        cell_id="auth-signup-otp-retry",
        parent=ids["container"],
        source=ids["otp_error"],
        target=ids["otp_input"],
        style=edge_style,
    )
    add_edge(
        root,
        cell_id="auth-signup-otp-valid",
        parent=ids["system_lane"],
        source=ids["otp_decision"],
        target=ids["personal_screen"],
        style=edge_style,
        label="Hợp lệ",
    )
    for number, (source, target) in enumerate(
        [
            (ids["personal_screen"], personal_input.get("id")),
            (personal_input.get("id"), personal_continue.get("id")),
            (personal_continue.get("id"), personal_validate.get("id")),
            (personal_validate.get("id"), password_screen.get("id")),
            (password_screen.get("id"), ids["password_input"]),
            (ids["password_input"], ids["register_click"]),
            (ids["register_click"], ids["save_account"]),
            (ids["save_account"], ids["return_sign_in"]),
            (ids["return_sign_in"], ids["end"]),
        ],
        1,
    ):
        add_edge(
            root,
            cell_id=f"auth-signup-finish-{number}",
            parent=ids["container"],
            source=source,
            target=target,
            style=edge_style,
        )


def reconcile_signin(document: ET.Element, config: dict) -> None:
    page = get_page(document, PAGE_SIGN_IN_PHONE, PAGE_SIGN_IN_EMAIL)
    page.set("name", PAGE_SIGN_IN_EMAIL)
    model, root = page_root(page)
    cells = index_cells(page)
    ids = config["signin"]
    edge_style = "edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;"
    action_style = cells[ids["credential_input"]].get("style", "")
    decision_style = cells[ids["decision"]].get("style", "")
    end_style = cells[ids["end"]].get("style", "")

    clear_edges(root)
    remove_cells(root, set(ids["remove"]))
    cells = index_cells(page)

    model.set("pageHeight", "1350")
    cells[ids["container"]].set("value", "Đăng nhập bằng email và mật khẩu")
    geometry(cells[ids["container"]]).set("height", "1240")
    geometry(cells[ids["actor_lane"]]).set("height", "1220")
    geometry(cells[ids["system_lane"]]).set("height", "1220")
    cells[ids["actor_lane"]].set("value", config["actor"])
    cells[ids["open"]].set("value", f"Mở app {config['app']}")
    cells[ids["credential_input"]].set("value", "Nhập email và mật khẩu")
    cells[ids["validate"]].set(
        "value", "Chuẩn hóa email và xác thực thông tin đăng nhập"
    )
    cells[ids["error"]].set(
        "value", "Hiển thị lỗi email hoặc mật khẩu không đúng; không tiết lộ tài khoản tồn tại"
    )
    cells[ids["save_session"]].set("value", "Lưu phiên đăng nhập")
    cells[ids["decision"]].set("value", "Thông tin đăng nhập hợp lệ?")

    positions = {
        "start": (190, 60, 40, 40),
        "open": (150, 140, 120, 60),
        "screen": (150, 140, 120, 60),
        "credential_input": (150, 260, 120, 60),
        "submit": (150, 380, 120, 60),
        "validate": (150, 380, 120, 60),
        "decision": (190, 500, 40, 40),
        "error": (40, 620, 120, 60),
        "save_session": (60, 900, 120, 60),
        "home": (60, 1020, 120, 60),
        "end": (105, 1140, 30, 30),
    }
    for key, box in positions.items():
        set_box(cells[ids[key]], *box)

    verified = add_vertex(
        root,
        cell_id="auth-email-verified",
        parent=ids["system_lane"],
        value="Email đã xác minh?",
        style=decision_style,
        x=280,
        y=760,
        width=40,
        height=40,
    )
    resume_otp = add_vertex(
        root,
        cell_id="auth-resume-signup-otp",
        parent=ids["system_lane"],
        value="Chuyển tới bước OTP của Đăng ký với email điền sẵn",
        style=action_style,
        x=240,
        y=900,
    )
    resume_end = add_vertex(
        root,
        cell_id="auth-resume-signup-end",
        parent=ids["system_lane"],
        value="",
        style=end_style,
        x=285,
        y=1020,
        width=30,
        height=30,
    )

    for number, (source, target) in enumerate(
        [
            (ids["start"], ids["open"]),
            (ids["open"], ids["screen"]),
            (ids["screen"], ids["credential_input"]),
            (ids["credential_input"], ids["submit"]),
            (ids["submit"], ids["validate"]),
            (ids["validate"], ids["decision"]),
        ],
        1,
    ):
        add_edge(
            root,
            cell_id=f"auth-signin-chain-{number}",
            parent=ids["container"],
            source=source,
            target=target,
            style=edge_style,
        )
    add_edge(
        root,
        cell_id="auth-signin-invalid",
        parent=ids["system_lane"],
        source=ids["decision"],
        target=ids["error"],
        style=edge_style,
        label="Không",
    )
    add_edge(
        root,
        cell_id="auth-signin-retry",
        parent=ids["container"],
        source=ids["error"],
        target=ids["credential_input"],
        style=edge_style,
    )
    add_edge(
        root,
        cell_id="auth-signin-valid",
        parent=ids["system_lane"],
        source=ids["decision"],
        target=verified.get("id"),
        style=edge_style,
        label="Có",
    )
    add_edge(
        root,
        cell_id="auth-signin-verified",
        parent=ids["system_lane"],
        source=verified.get("id"),
        target=ids["save_session"],
        style=edge_style,
        label="Có",
    )
    add_edge(
        root,
        cell_id="auth-signin-unverified",
        parent=ids["system_lane"],
        source=verified.get("id"),
        target=resume_otp.get("id"),
        style=edge_style,
        label="Chưa",
        label_x=0,
        label_offset_x=28,
        label_offset_y=-16,
    )
    for number, (source, target) in enumerate(
        [
            (ids["save_session"], ids["home"]),
            (ids["home"], ids["end"]),
            (resume_otp.get("id"), resume_end.get("id")),
        ],
        1,
    ):
        add_edge(
            root,
            cell_id=f"auth-signin-finish-{number}",
            parent=ids["system_lane"],
            source=source,
            target=target,
            style=edge_style,
        )


def reconcile_signout(document: ET.Element, config: dict) -> None:
    page = get_page(document, "AD_Sign Out")
    model, root = page_root(page)
    cells = index_cells(page)
    ids = config["signout"]
    edge_style = "edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;"

    clear_edges(root)
    remove_cells(root, set(ids["remove"]))
    cells = index_cells(page)

    model.set("pageHeight", "1200")
    geometry(cells[ids["container"]]).set("height", "1080")
    geometry(cells[ids["actor_lane"]]).set("height", "1060")
    geometry(cells[ids["system_lane"]]).set("height", "1060")
    cells[ids["actor_lane"]].set("value", config["actor"])
    cells[ids["open"]].set("value", f"Mở app {config['app']} với phiên đăng nhập còn hiệu lực")
    cells[ids["revoke"]].set(
        "value", "Thu hồi phiên đăng nhập hiện tại và xóa credential trên client"
    )
    cells[ids["sign_in_screen"]].set("value", "Hiển thị màn hình Đăng nhập")

    positions = {
        "start": (190, 60, 40, 40),
        "open": (150, 140, 120, 60),
        "home": (150, 260, 120, 60),
        "menu_click": (150, 380, 120, 60),
        "menu_screen": (150, 500, 120, 60),
        "signout_click": (150, 620, 120, 60),
        "revoke": (150, 740, 120, 60),
        "sign_in_screen": (150, 860, 120, 60),
        "end": (195, 980, 30, 30),
    }
    for key, box in positions.items():
        set_box(cells[ids[key]], *box)

    for number, (source, target) in enumerate(
        [
            (ids["start"], ids["open"]),
            (ids["open"], ids["home"]),
            (ids["home"], ids["menu_click"]),
            (ids["menu_click"], ids["menu_screen"]),
            (ids["menu_screen"], ids["signout_click"]),
            (ids["signout_click"], ids["revoke"]),
            (ids["revoke"], ids["sign_in_screen"]),
            (ids["sign_in_screen"], ids["end"]),
        ],
        1,
    ):
        add_edge(
            root,
            cell_id=f"auth-signout-chain-{number}",
            parent=ids["container"],
            source=source,
            target=target,
            style=edge_style,
        )


def reconcile_forgot_password(document: ET.Element, config: dict) -> None:
    page = get_page(document, "AD_Forgot Password")
    model, root = page_root(page)
    cells = index_cells(page)
    ids = config["forgot"]
    edge_style = "edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;"
    action_style = cells[ids["email_input"]].get("style", "")

    clear_edges(root)
    remove_cells(root, set(ids["remove"]))
    cells = index_cells(page)

    model.set("pageHeight", "2150")
    geometry(cells[ids["container"]]).set("height", "2020")
    geometry(cells[ids["actor_lane"]]).set("height", "2000")
    geometry(cells[ids["system_lane"]]).set("height", "2000")
    cells[ids["actor_lane"]].set("value", config["actor"])
    cells[ids["open"]].set("value", f"Mở app {config['app']}")
    cells[ids["email_input"]].set("value", "Nhập email đã dùng để đăng ký tài khoản")
    cells[ids["email_check"]].set(
        "value", "Chuẩn hóa email; kiểm tra định dạng và rate limit"
    )
    cells[ids["eligibility"]].set("value", "Tài khoản đủ điều kiện recovery?")
    cells[ids["no_send"]].set("value", "Không gửi OTP")
    cells[ids["send_otp"]].set("value", "Gửi OTP 6 chữ số tới email")
    cells[ids["otp_screen"]].set(
        "value", "Hiển thị phản hồi trung tính và màn hình nhập OTP"
    )
    cells[ids["otp_input"]].set("value", "Nhập mã OTP nhận qua email")
    cells[ids["otp_submit"]].set("value", "Bấm nút Tiếp tục")
    cells[ids["otp_verify"]].set("value", "Xác thực mã OTP")
    cells[ids["otp_decision"]].set("value", "OTP hợp lệ và còn hạn?")
    cells[ids["password_screen"]].set(
        "value", "Cấp reset token one-time và hiển thị màn hình nhập mật khẩu mới"
    )
    cells[ids["otp_error"]].set(
        "value", "Báo lỗi OTP sai, hết hạn hoặc vượt số lần thử"
    )
    cells[ids["password_input"]].set(
        "value", "Nhập mật khẩu mới và xác nhận mật khẩu mới"
    )
    cells[ids["save_password"]].set(
        "value", "Cập nhật mật khẩu và thu hồi toàn bộ phiên đăng nhập"
    )
    cells[ids["return_sign_in"]].set(
        "value", "Về Đăng nhập với email điền sẵn; không auto-login"
    )

    positions = {
        "start": (190, 60, 40, 40),
        "open": (150, 140, 120, 60),
        "sign_in_screen": (150, 140, 120, 60),
        "forgot_link": (150, 260, 120, 60),
        "forgot_screen": (150, 360, 120, 60),
        "email_input": (150, 460, 120, 60),
        "email_check": (150, 580, 120, 60),
        "eligibility": (190, 680, 40, 40),
        "send_otp": (60, 800, 120, 60),
        "no_send": (260, 800, 120, 60),
        "otp_screen": (150, 920, 120, 60),
        "otp_input": (150, 1040, 120, 60),
        "otp_submit": (150, 1160, 120, 60),
        "otp_verify": (150, 1160, 120, 60),
        "otp_decision": (190, 1280, 40, 40),
        "password_screen": (60, 1400, 120, 60),
        "otp_error": (240, 1400, 120, 60),
        "password_input": (150, 1520, 120, 60),
        "password_submit": (150, 1640, 120, 60),
        "password_check": (150, 1640, 120, 60),
        "save_password": (150, 1740, 120, 60),
        "return_sign_in": (150, 1840, 120, 60),
        "end": (195, 1940, 30, 30),
    }
    for key, box in positions.items():
        set_box(cells[ids[key]], *box)

    email_submit = add_vertex(
        root,
        cell_id="auth-forgot-email-submit",
        parent=ids["actor_lane"],
        value="Bấm nút Gửi OTP",
        style=action_style,
        x=150,
        y=580,
    )

    for number, (source, target) in enumerate(
        [
            (ids["start"], ids["open"]),
            (ids["open"], ids["sign_in_screen"]),
            (ids["sign_in_screen"], ids["forgot_link"]),
            (ids["forgot_link"], ids["forgot_screen"]),
            (ids["forgot_screen"], ids["email_input"]),
            (ids["email_input"], email_submit.get("id")),
            (email_submit.get("id"), ids["email_check"]),
            (ids["email_check"], ids["eligibility"]),
        ],
        1,
    ):
        add_edge(
            root,
            cell_id=f"auth-forgot-chain-{number}",
            parent=ids["container"],
            source=source,
            target=target,
            style=edge_style,
        )
    add_edge(
        root,
        cell_id="auth-forgot-eligible",
        parent=ids["system_lane"],
        source=ids["eligibility"],
        target=ids["send_otp"],
        style=edge_style,
        label="Có",
    )
    add_edge(
        root,
        cell_id="auth-forgot-ineligible",
        parent=ids["system_lane"],
        source=ids["eligibility"],
        target=ids["no_send"],
        style=edge_style,
        label="Không",
    )
    for number, source in enumerate([ids["send_otp"], ids["no_send"]], 1):
        add_edge(
            root,
            cell_id=f"auth-forgot-join-{number}",
            parent=ids["system_lane"],
            source=source,
            target=ids["otp_screen"],
            style=edge_style,
        )
    for number, (source, target) in enumerate(
        [
            (ids["otp_screen"], ids["otp_input"]),
            (ids["otp_input"], ids["otp_submit"]),
            (ids["otp_submit"], ids["otp_verify"]),
            (ids["otp_verify"], ids["otp_decision"]),
        ],
        1,
    ):
        add_edge(
            root,
            cell_id=f"auth-forgot-otp-{number}",
            parent=ids["container"],
            source=source,
            target=target,
            style=edge_style,
        )
    add_edge(
        root,
        cell_id="auth-forgot-otp-valid",
        parent=ids["system_lane"],
        source=ids["otp_decision"],
        target=ids["password_screen"],
        style=edge_style,
        label="Hợp lệ",
    )
    add_edge(
        root,
        cell_id="auth-forgot-otp-invalid",
        parent=ids["system_lane"],
        source=ids["otp_decision"],
        target=ids["otp_error"],
        style=edge_style,
        label="Không hợp lệ",
    )
    add_edge(
        root,
        cell_id="auth-forgot-otp-retry",
        parent=ids["container"],
        source=ids["otp_error"],
        target=ids["otp_input"],
        style=edge_style,
    )
    for number, (source, target) in enumerate(
        [
            (ids["password_screen"], ids["password_input"]),
            (ids["password_input"], ids["password_submit"]),
            (ids["password_submit"], ids["password_check"]),
            (ids["password_check"], ids["save_password"]),
            (ids["save_password"], ids["return_sign_in"]),
            (ids["return_sign_in"], ids["end"]),
        ],
        1,
    ):
        add_edge(
            root,
            cell_id=f"auth-forgot-finish-{number}",
            parent=ids["container"],
            source=source,
            target=target,
            style=edge_style,
        )


def reconcile_file(source: Path, output: Path, app: str) -> None:
    tree = ET.parse(source)
    document = tree.getroot()
    config = APP_CONFIG[app]
    reconcile_signup(document, config)
    reconcile_signin(document, config)
    reconcile_signout(document, config)
    reconcile_forgot_password(document, config)
    for page_name in [
        PAGE_SIGN_UP_EMAIL,
        PAGE_SIGN_IN_EMAIL,
        "AD_Sign Out",
        "AD_Forgot Password",
    ]:
        normalize_auth_page(get_page(document, page_name))
    ET.indent(tree, space="  ")
    output.parent.mkdir(parents=True, exist_ok=True)
    tree.write(output, encoding="utf-8", xml_declaration=False)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--app", choices=sorted(APP_CONFIG), required=True)
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    reconcile_file(args.input, args.output, args.app)


if __name__ == "__main__":
    main()
