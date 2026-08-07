#!/usr/bin/env python3
"""六十日教本 — 巻二（データ通信技術60日講座）のデータを index.html に注入する。

build/net/week1.js 〜 week9.js を読み、index.html 内の
    <!-- NET:START --> ... <!-- NET:END -->
で囲まれた領域を丸ごと差し替える。何度実行しても同じ結果になる。

使い方:
    python3 build/assemble.py
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
INDEX = ROOT / "index.html"
NETDIR = pathlib.Path(__file__).resolve().parent / "net"

START = "<!-- NET:START -->"
END = "<!-- NET:END -->"


def build_block() -> str:
    parts = [START]
    for w in range(1, 10):
        src = NETDIR / f"week{w}.js"
        if not src.exists():
            sys.exit(f"missing: {src}")
        parts.append("<script>")
        parts.append(src.read_text(encoding="utf-8").rstrip())
        parts.append("</script>")
    parts.append(END)
    return "\n".join(parts)


def main() -> None:
    html = INDEX.read_text(encoding="utf-8")
    if START not in html or END not in html:
        sys.exit(f"markers not found in {INDEX}. 手動での初回組み込みが必要です。")

    pattern = re.compile(re.escape(START) + r".*?" + re.escape(END), re.DOTALL)
    new_html = pattern.sub(lambda _: build_block(), html, count=1)
    INDEX.write_text(new_html, encoding="utf-8")

    days = len(re.findall(r"NET\.push\(\{", build_block()))
    print(f"注入完了: {days} 日分 / {INDEX.stat().st_size:,} バイト")


if __name__ == "__main__":
    main()
