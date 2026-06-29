# VER-Lib マニュアル — Sphinx 設定
# 実行: sphinx-build -W -b html -c . pages _build/html
#       (conf.py = repo root、source = pages/、-c でconfig dirをrootに固定)

project = "VER-Lib マニュアル"
author = "VER-Lib Team"
copyright = "2026, VER-Lib Team"
language = "ja"

extensions = [
    "myst_parser",
]

# MyST: コールアウト(colon_fence)・LaTeX数式(dollarmath/amsmath)・定義リスト
myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "dollarmath",
    "amsmath",
]

source_suffix = {".md": "markdown"}
root_doc = "index"

templates_path = ["pages/_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", "**/.gitkeep"]

# 軽量・依存追加なしの組込みテーマ
html_theme = "alabaster"
html_static_path = ["pages/_static"]
html_title = "VER-Lib マニュアル"
