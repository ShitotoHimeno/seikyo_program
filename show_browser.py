import streamlit as st
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

# --- データベース接続とデータ取得 ---
# データベースパスをスクリプトからの相対パスに変更することを推奨します
DB_PATH = 'seikyo_db.db'
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
    join order_table o on d.order_id = o.order_id
    join item_table i on d.item_id = i.item_id
"""
order_detail_table = pd.read_sql_query(query, conn)
conn.close()

# --- データ加工と集計 ---
# 日付データをdatetime型に変換
order_detail_table["order_date"] = pd.to_datetime(order_detail_table["order_date"])
order_detail_table["money"] = order_detail_table["quantity"] * order_detail_table["price"]
money_sum_by_date = order_detail_table.groupby("order_date")["money"].sum().reset_index()

# --- Matplotlibの日本語フォント設定 ---
# Windowsの日本語フォントをfont.sans-serifのリストに追加
plt.rcParams['font.sans-serif'] = ['Yu Gothic', 'Meiryo', 'TakaoGothic']
# Axesの文字化けを防ぐため、Unicode minusを無効化
plt.rcParams['axes.unicode_minus'] = False

# --- Streamlitでグラフを表示 ---
st.title("注文ごとの売上金額の推移")

fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(money_sum_by_date["order_date"], money_sum_by_date["money"], marker='o', label="日別売上")
ax.set_title("日別売上金額の推移")
ax.set_xlabel("注文日")
ax.set_ylabel("売上金額")
ax.legend()
ax.grid(True)

st.pyplot(fig)