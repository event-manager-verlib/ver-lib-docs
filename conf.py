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

# モダンな Furo をベースに、event-manager-design-system 準拠でカスタム化。
# 色/フォントは design-system の semantic tokens に対応
# (SSoT = event-manager-design-system/build/css/variables.css)。
# tokens 改訂時は下記 html_theme_options + pages/_static/custom.css を追従させる。
html_theme = "furo"
html_static_path = ["pages/_static"]
html_title = "VER-Lib マニュアル"
html_css_files = ["custom.css"]

html_theme_options = {
    # --- light (お菓子パレット: cream 地 / bitterChoco 文字) ---
    "light_css_variables": {
        "color-brand-primary": "#8C7667",      # almond.dark  (見出し/現在地アクセント)
        "color-brand-content": "#A68465",      # caramel.dark (本文リンク)
        "color-brand-visited": "#A9B298",      # pistachio.dark
        "color-background-primary": "#FBF9F6",   # cream.main   (本文背景)
        "color-background-secondary": "#F2EFEC", # cacao.light  (サイドバー)
        "color-background-hover": "#EBE9E6",     # cream.dark
        "color-foreground-primary": "#564C45",   # bitterChoco.main (本文)
        "color-foreground-secondary": "#665A52", # bitterChoco.light
        "color-foreground-muted": "#9E8879",     # almond.main
        "color-foreground-border": "#C3BDB7",    # milkCocoa.main
        "color-background-border": "#D9D6D1",    # cacao.dark
        "color-api-background": "#F2EFEC",
        "font-stack": '"M PLUS Rounded 1c", Roboto, "Helvetica", Arial, sans-serif',
    },
    # --- dark (同色相を反転: bitterChoco 地 / cream 文字、pistachio アクセント) ---
    "dark_css_variables": {
        "color-brand-primary": "#C5CEB4",      # pistachio.light
        "color-brand-content": "#C5CEB4",
        "color-brand-visited": "#C4A283",      # caramel.light
        "color-background-primary": "#473E38",   # bitterChoco.dark
        "color-background-secondary": "#3E362F",
        "color-background-hover": "#564C45",     # bitterChoco.main
        "color-foreground-primary": "#FBF9F6",   # cream.main
        "color-foreground-secondary": "#E8E5E0", # cacao.main
        "color-foreground-muted": "#C3BDB7",     # milkCocoa.main
        "color-foreground-border": "#665A52",    # bitterChoco.light
        "color-background-border": "#665A52",
        "color-api-background": "#3E362F",
        "font-stack": '"M PLUS Rounded 1c", Roboto, "Helvetica", Arial, sans-serif',
    },
}
