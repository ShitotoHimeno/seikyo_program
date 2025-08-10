import sqlite3
import pandas as pd

# データベースファイルのパスを指定
db_path = r'C:\Users\kudom\.vscode\seikyo_db\seikyo_db.db'

# データベースに接続
conn = sqlite3.connect(db_path)

# CSVファイルのパスを指定し、それぞれのデータフレームに読み込む
producers_df = pd.read_csv(r'C:\Users\kudom\.vscode\seikyo_db\producers.csv')
customers_df = pd.read_csv(r'C:\Users\kudom\.vscode\seikyo_db\customers.csv')
items_df = pd.read_csv(r'C:\Users\kudom\.vscode\seikyo_db\items.csv')
orders_df = pd.read_csv(r'C:\Users\kudom\.vscode\seikyo_db\orders.csv')
# order_details_df = pd.read_csv(r'C:\Users\kudom\.vscode\seikyo_db\order_details.csv') # 必要に応じてコメントアウトを外す

# データフレームを対応するテーブルに挿入
producers_df.to_sql('producer_table', conn, if_exists='append', index=False)
customers_df.to_sql('customer_table', conn, if_exists='append', index=False)
items_df.to_sql('item_table', conn, if_exists='append', index=False)
orders_df.to_sql('order_table', conn, if_exists='append', index=False)
# order_details_df.to_sql('order_detail_table', conn, if_exists='append', index=False) # 必要に応じてコメントアウトを外す

# 変更をコミット
conn.commit()

# 接続を閉じる
conn.close()

print("データの挿入が完了しました。")