import streamlit as st
import pandas as pd
import sqlite3
import os

DB_PATH = r'C:\Users\kudom\.vscode\seikyo_db\seikyo_db.db'

conn = sqlite3.connect(DB_PATH)

query = """
select
    d.order_detail_id,
    d.order_id,
    d.item_id,
    d.quantity,
    o.order_date,
    i.item_name,
    i.price
from
    order_detail_table d
    join item_table i on d.item_id = i.item_id
    join order_table o on d.order_id = o.order_id

"""


order_detail_table = pd.read_sql_query(query, conn)

conn.close()

print("order_detail_tableのデータを取得しました。")
print(order_detail_table.head())





