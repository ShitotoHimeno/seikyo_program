# #ダミーデータをSQLiteデータベースに挿入するスクリプトなので一旦コメントアウトしておきます。
# import sqlite3
# import pandas as pd

# # データベースファイルのパスを指定
# db_path = r'C:\Users\kudom\.vscode\seikyo_db\seikyo_db.db'

# # データベースに接続
# conn = sqlite3.connect(db_path)

# # CSVファイルのパスを指定し、それぞれのデータフレームに読み込む
# producers_df = pd.read_csv(r'C:\Users\kudom\.vscode\seikyo_db\producers.csv')
# customers_df = pd.read_csv(r'C:\Users\kudom\.vscode\seikyo_db\customers.csv')
# items_df = pd.read_csv(r'C:\Users\kudom\.vscode\seikyo_db\items.csv')
# orders_df = pd.read_csv(r'C:\Users\kudom\.vscode\seikyo_db\orders.csv')
# # order_details_df = pd.read_csv(r'C:\Users\kudom\.vscode\seikyo_db\order_details.csv') # 必要に応じてコメントアウトを外す

# # データフレームを対応するテーブルに挿入
# producers_df.to_sql('producer_table', conn, if_exists='append', index=False)
# customers_df.to_sql('customer_table', conn, if_exists='append', index=False)
# items_df.to_sql('item_table', conn, if_exists='append', index=False)
# orders_df.to_sql('order_table', conn, if_exists='append', index=False)
# # order_details_df.to_sql('order_detail_table', conn, if_exists='append', index=False) # 必要に応じてコメントアウトを外す

# # 変更をコミット
# conn.commit()

# # 接続を閉じる
# conn.close()

# print("データの挿入が完了しました。")

import sqlite3

DB_PATH = 'seikyo_db.db'
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

dummy_data_sql = """
INSERT INTO item_table (
    item_id, item_name, item_category, price, created_date, update_date, producer_id
) VALUES
(1000, 'ダミーアイテム-000', 'ダミーカテゴリ', 500, '2025-08-11', '2025-08-11', 1),
(1001, 'ダミーアイテム-001', 'ダミーカテゴリ', 510, '2025-08-11', '2025-08-11', 1),
(1002, 'ダミーアイテム-002', 'ダミーカテゴリ', 520, '2025-08-11', '2025-08-11', 1),
(1003, 'ダミーアイテム-003', 'ダミーカテゴリ', 530, '2025-08-11', '2025-08-11', 1),
(1004, 'ダミーアイテム-004', 'ダミーカテゴリ', 540, '2025-08-11', '2025-08-11', 1),
(1005, 'ダミーアイテム-005', 'ダミーカテゴリ', 550, '2025-08-11', '2025-08-11', 1),
(1006, 'ダミーアイテム-006', 'ダミーカテゴリ', 560, '2025-08-11', '2025-08-11', 1),
(1007, 'ダミーアイテム-007', 'ダミーカテゴリ', 570, '2025-08-11', '2025-08-11', 1),
(1008, 'ダミーアイテム-008', 'ダミーカテゴリ', 580, '2025-08-11', '2025-08-11', 1),
(1009, 'ダミーアイテム-009', 'ダミーカテゴリ', 590, '2025-08-11', '2025-08-11', 1);
"""

try:
    cursor.execute(dummy_data_sql)
    conn.commit() # 変更を保存
    print("ダミーデータを10件挿入しました。")
except sqlite3.IntegrityError as e:
    print(f"データの挿入に失敗しました: {e}")

conn.close()