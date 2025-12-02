# kakeibo-app
Python と SQLiteを使ったシンプルな家計簿アプリです。

CLIから収入・支出を簡単に登録でき、データは SQLite に保存されます。

今後は Streamlit を用いた GUI 版の開発も予定しています。

---

## Features （機能）
-収入・支出の登録（ターミナルから入力）

-日付・カテゴリ・金額・メモを SQLite に保存

-登録データの一覧表示

-DB はローカルに自動生成（'kakeibo.db'）

-GitHub には DB を公開しない設計（'.gitignore' で除外）

---

## How to Run （実行方法）

1.リポジトリをクローン

git clone https://github.com/shota-tdkr/kakeibo-app.git

cd kakeibo-app

2.Python スクリプトを実行

python kakibo_cli.py

---

## Directory Structure（ディレクトリ構成）
kakeibo-app/

|────kakeibo_cli.py    # メインのターミナル版家計簿アプリ

|────kakeibo.db        

|────README.md

└────.gitignore

---

## Tech Stack（技術）
- Python 3.x
  
- SQLite3

- Git / GitHub

---

## Future Work（今後の拡張予定）
- Streamlit を用いた Web 版家計簿

- 月ごとの集計機能（グラフ）

- カテゴリごとの支出割合可視化

- CSV エクスポート機能

---

## License
This software is released under the MIT License.