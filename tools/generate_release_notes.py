#!/usr/bin/env python3
"""リリースノートページ (pages/06_付録/02_release_note.md) を releases.json から生成する。

SSoT は別リポ event-manager-release-notes の data/releases.json。
このスクリプトはそれを読んで、マニュアル掲載用の Markdown を生成する
(= マニュアルとアプリ内お知らせの内容が乖離しないようにするため)。

releases.json の探索順:
  1. 環境変数 VERLIB_RELEASES_JSON (明示指定)
  2. external/release-notes/data/releases.json     (CI: release-notes リポを checkout した場所)
  3. ../event-manager-release-notes/data/releases.json  (ローカル workspace の sibling)

いずれも見つからなければ **何もしない** (既存のコミット済み md をそのまま使う)。
これにより、release-notes を持たないローカル環境でも sphinx-build は失敗しない。

conf.py の setup() から呼ばれるほか、単体でも実行できる:
    python tools/generate_release_notes.py
"""
from __future__ import annotations

import json
import os
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
OUTPUT = REPO_ROOT / "pages" / "06_付録" / "02_release_note.md"

CANDIDATES = [
    os.environ.get("VERLIB_RELEASES_JSON"),
    str(REPO_ROOT / "external" / "release-notes" / "data" / "releases.json"),
    str(REPO_ROOT.parent / "event-manager-release-notes" / "data" / "releases.json"),
]

TYPE_JA = {
    "feature": "新機能",
    "fix": "修正",
    "improvement": "改善",
    "notice": "お知らせ",
}
APP_JA = {"event": "イベント管理", "guest": "ゲスト", "staff": "スタッフ"}
ALL_APPS = {"event", "guest", "staff"}

HEADER = """<!-- このファイルは tools/generate_release_notes.py により releases.json から自動生成されます。手で編集しないでください (SSoT = event-manager-release-notes/data/releases.json)。 -->

# リリースノート

VER-Lib の新機能や改善のお知らせです。ここに掲載する内容は、各アプリ（イベント管理 / スタッフ / ゲスト）を開いたときにも、お知らせとして表示されます。各項目の末尾は対象アプリを表します。
"""


def _apps_label(apps: list[str]) -> str:
    s = set(apps)
    if s == ALL_APPS:
        return "全アプリ"
    # releases.json の並び (event, guest, staff) を保ってラベル化
    order = ["event", "guest", "staff"]
    return "・".join(APP_JA.get(a, a) for a in order if a in s)


def _find_json() -> Path | None:
    for c in CANDIDATES:
        if c and Path(c).is_file():
            return Path(c)
    return None


def render(data: dict) -> str:
    lines = [HEADER]
    for rel in data.get("releases", []):
        version = rel["version"]
        released_at = rel.get("released_at", "")
        title = rel.get("title", "")
        heading = f"## {version}（{released_at}）{title}".rstrip("（）")
        lines.append("")
        lines.append(heading)
        lines.append("")
        rel_apps = rel.get("apps", [])
        for h in rel.get("highlights", []):
            type_ja = TYPE_JA.get(h.get("type", ""), h.get("type", ""))
            apps = h.get("apps") or rel_apps
            apps_label = _apps_label(apps)
            text = h.get("text", "").strip()
            lines.append(f"- **{type_ja}**（{apps_label}）— {text}")
    return "\n".join(lines) + "\n"


def main() -> None:
    src = _find_json()
    if src is None:
        print("[release-notes] releases.json が見つかりません。生成をスキップします。")
        return
    data = json.loads(src.read_text(encoding="utf-8"))
    OUTPUT.write_text(render(data), encoding="utf-8")
    print(f"[release-notes] {src} -> {OUTPUT} ({len(data.get('releases', []))} releases)")


if __name__ == "__main__":
    main()
