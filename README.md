# ver-lib-docs

イベント管理プロダクト **VER-Lib** の公式マニュアル（運用者 / エンドユーザー向け）。

- 執筆: `pages/` 配下の Markdown (MyST)
- ビルド: Sphinx + MyST-Parser
- 公開: GitHub Actions → GitHub Pages（`main` merge で自動）

## ローカルビルド

```bash
pip install -r requirements.txt
sphinx-build -W -b html -c . pages _build/html
# open _build/html/index.html
```

執筆ルール・環境セットアップは `pages/05_dev_guide/doc_rules.md` と
ワークスペースの `.agent/TBD/機能追加/ver_lib_manual_documentation_plan.md` を参照。
