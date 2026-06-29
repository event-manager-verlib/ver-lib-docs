# ドキュメント執筆ルール

執筆者によるドキュメントのブレを防ぐため、以下の記述ルールに準拠してください。本ページはマニュアルの記法 SSoT です。

## ① 見出しのルール

ページのタイトルは `#` (H1) とし、**1 ページ内に 1 つだけ**にします。セクションは `##` (H2)、その下は `###` (H3) とし、H4 以下は極力避けてページを分割してください。

## ② コールアウト（警告やヒント）

MyST-Parser の Admonitions を活用し、注意や重要なメモを目立たせます。

````{note}
```{note}
これは重要な補足情報です。環境設定を誤ると、ライブラリが正しく動作しない恐れがあります。
```
````

`{note}` のほか `{warning}` `{tip}` `{important}` などが利用できます。

## ③ コード・数式

- 変数名やファイル名はインラインコード（`` `code` ``）で囲みます。
- 数式は LaTeX スタイルで記述します。
  - インライン数式: `$E = mc^2$`
  - ブロック数式: `$$ \sum_{i=1}^{n} i = \frac{n(n+1)}{2} $$`

## ④ 画像の挿入

画像は `pages/_static/` ディレクトリに配置し、相対パスで参照します。

```markdown
![VER-Libの全体構成図](../_static/architecture_diagram.png)
```

## ⑤ 目次への登録と表示順

各ページはトップの [`index.md`](../index.md) の `{toctree}`（`:glob:`）が自動巡回します。表示順は**ファイル名のアルファベット / 数値順**です。順序を制御したい場合はファイル名に数値プレフィックス（例: `01_`, `02_`）を付けてください。

## ⑥ ビルド検証（執筆フロー）

PR を出す前に、ローカルで warning 0 のビルドを確認してください（CI も同じチェックを必須化しています）。

```bash
pip install -r requirements.txt
sphinx-build -W -b html -c . pages _build/html      # warnings-as-errors
sphinx-build -b linkcheck -c . pages _build/linkcheck # 内部リンク切れ検出
```

`main` への merge で GitHub Actions が自動でビルド・公開します。
