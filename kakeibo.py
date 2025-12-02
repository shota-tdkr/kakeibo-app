#
import sqlite3
import os

#DBに接続
conn = sqlite3.connect("kakeibo.db")    #DBファイルがなければ作成される

#テーブル作成
conn.execute("""
              CREATE TABLE IF NOT EXISTS records (
                  id INTEGER PRIMARY KEY AUTOINCREMENT,
                  date TEXT,
                  category TEXT,
                  amount INTEGER,
                  memo TEXT
              )
              """)
conn.commit()   #変更を保存

#レコードを一件追加
conn.execute("""
             INSERT INTO record (date, category, amount, memo)
             VALUES ('2025-12-02', '食費', 1500, 'ランチ代')
             """)
conn.commit()   #変更を保存

#全レコード取得して表示
rows = conn.execute("SELECT * FROM records").fetchall()
for row in rows:
    print(row)

#接続を閉じる
conn.close()