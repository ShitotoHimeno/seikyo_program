import sqlite3
import pandas as pd

# データベースファイルのパスを指定
db_path = 'seikyo_db.db' 

# データベースに接続
conn = sqlite3.connect(db_path)

# ...existing code...
producers_df = pd.read_csv(r'C:\Users\kudom\.vscode\seikyo_db\customers.csv')
customers_df = pd.read_csv(r'C:\Users\kudom\.vscode\seikyo_db\customers.csv')
items_df = pd.read_csv(r'C:\Users\kudom\.vscode\seikyo_db\items.csv')
orders_df = pd.read_csv(r'C:\Users\kudom\.vscode\seikyo_db\orders.csv')
# ...existing code...
# order_details_df = pd.read_csv('seikyo_db/order_details.csv')
# 接続を閉じる

conn.close()

print("データの挿入が完了しました。")