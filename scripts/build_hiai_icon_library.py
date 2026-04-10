#!/usr/bin/env python3
"""Scan ./hiai icon svg/*.svg and emit icon-library/HiAI-*.json + manifest snippet."""
from __future__ import annotations

import json
import re
from pathlib import Path
from urllib.parse import quote

REPO = Path(__file__).resolve().parents[1]
SVG_DIR = REPO / "hiai icon svg"
OUT_DIR = REPO / "icon-library"
MANIFEST = OUT_DIR / "manifest.json"

# First matching category wins (substring match on lowercased filename stem).
CATEGORIES: list[tuple[str, str, list[str]]] = [
    (
        "HiAI-Editor",
        "HiAI · 文本与排版",
        [
            "text", "bold", "italic", "underline", "strikethrough", "list", "align",
            "indent", "heading", "type-", "font", "paragraph", "subscript", "superscript",
            "pen-tool", "pen_", "order", "bullet", "disorder-list", "ordered_list",
            "highlighter", "eraser", "quote", "spacing-", "skew", "perspective",
            "rows-01", "columns-01", "tab_arrow", "tabs_", "layer", "component",
        ],
    ),
    (
        "HiAI-Users",
        "HiAI · 用户与成员",
        [
            "user", "users", "member", "people", "person", "face", "avatar", "profile",
            "contact", "passport", "passkey", "fingerprint",
        ],
    ),
    (
        "HiAI-Communication",
        "HiAI · 沟通与通知",
        [
            "mail", "message", "chat", "phone", "send", "reply", "announcement",
            "megaphone", "inbox", "share", "at-sign", "notification", "bell", "sms",
        ],
    ),
    (
        "HiAI-Files",
        "HiAI · 文件与存储",
        [
            "file", "folder", "package", "save", "download", "upload", "attachment",
            "paperclip", "clipboard", "archive", "tray", "inbox-",
        ],
    ),
    (
        "HiAI-Charts",
        "HiAI · 图表与数据",
        [
            "chart", "graph", "pie", "bar-chart", "bar_chart", "trend", "presentation",
            "stat", "analytics", "percent", "grid", "table", "rows-", "columns-",
            "data-", "ranking", "stack_bar", "true_false", "thermometer",
        ],
    ),
    (
        "HiAI-Media",
        "HiAI · 媒体与播放",
        [
            "image", "video", "play", "pause", "music", "camera", "volume", "microphone",
            "film", "airplay", "tv-", "record", "photo", "subtitles", "headphones",
            "airpods", "speaker",
        ],
    ),
    (
        "HiAI-Development",
        "HiAI · 开发与代码",
        [
            "code", "terminal", "server", "database", "git", "branch", "commit", "cpu",
            "chip", "dataflow", "plugin", "puzzle", "variable", "if-", "stack_", "api",
            "webhook", "bug", "script", "container", "docker", "binary",
        ],
    ),
    (
        "HiAI-Interface",
        "HiAI · 界面与导航",
        [
            "menu", "layout", "grid", "tab", "window", "home", "search", "filter",
            "settings", "slider", "toggle", "dots", "more-", "maximize", "minimize",
            "trash", "edit", "plus", "minus", "check", "close", "arrow", "chevron",
            "sidebar", "monitor", "calendar", "clock", "alarm", "sun", "moon", "zap",
            "power", "log-in", "log-out", "refresh", "rotate", "move", "drag", "eye",
            "scan", "target", "link-", "navigation", "route", "map", "marker-pin",
            "globe", "wifi", "bluetooth", "battery", "plug", "tool", "wrench",
            "lock", "key", "shield", "alert", "info", "help", "question",
        ],
    ),
]

DEFAULT_CAT = ("HiAI-General", "HiAI · 通用", [])


def stem_norm(name: str) -> str:
    stem = Path(name).stem
    s = re.sub(r"([a-z0-9])([A-Z])", r"\1-\2", stem)
    s = re.sub(r"([A-Z]+)([A-Z][a-z])", r"\1-\2", s)
    s = s.replace("_", "-")
    s = re.sub(r"[^a-zA-Z0-9]+", "-", s.lower()).strip("-")
    return s or "icon"


def svg_url(filename: str) -> str:
    folder = quote("hiai icon svg", safe="")
    fn = quote(filename, safe="")
    return f"./{folder}/{fn}"


def classify(stem_lower: str) -> tuple[str, str]:
    for cat_id, label, keys in CATEGORIES:
        for k in keys:
            if k in stem_lower:
                return cat_id, label
    return DEFAULT_CAT[0], DEFAULT_CAT[1]


def main() -> None:
    if not SVG_DIR.is_dir():
        raise SystemExit(f"Missing SVG dir: {SVG_DIR}")

    buckets: dict[str, list[dict]] = {c[0]: [] for c in CATEGORIES}
    buckets[DEFAULT_CAT[0]] = []

    for path in sorted(SVG_DIR.glob("*.svg")):
        stem = stem_norm(path.name)
        name = f"hiai-{stem}"
        cat_id, _ = classify(stem)
        buckets[cat_id].append(
            {
                "name": name,
                "url": svg_url(path.name),
                "inset": "inset-[8.33%]",
            }
        )

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for cat_id, icons in buckets.items():
        out = OUT_DIR / f"{cat_id}.json"
        out.write_text(json.dumps({"icons": icons}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"{cat_id}: {len(icons)} -> {out.name}")

    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    cats = manifest.get("categories", [])
    existing_ids = {c.get("id") for c in cats if isinstance(c, dict)}

    for cat_id, label, _ in CATEGORIES + [DEFAULT_CAT]:
        if cat_id in existing_ids:
            continue
        n = len(buckets.get(cat_id, []))
        cats.append(
            {
                "id": cat_id,
                "label": label,
                "count": n,
                "file": f"{cat_id}.json",
            }
        )
        existing_ids.add(cat_id)

    # Refresh counts for HiAI categories
    for c in cats:
        cid = c.get("id")
        if cid in buckets:
            c["count"] = len(buckets[cid])

    manifest["categories"] = cats
    manifest["generatedFrom"] = manifest.get("generatedFrom", "") + " +local:hiai-icon-svg"
    MANIFEST.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("Updated manifest.json")


if __name__ == "__main__":
    main()
