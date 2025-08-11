import streamlit as st
import pandas as pd
import sqlite3
import os

# データベースファイルのパスを指定
DB_PATH = r'C:\Users\kudom\.vscode\seikyo_db\seikyo_db.db'

# データベース接続関数
@st.cache_resource
def get_db_connection():
    """データベース接続オブジェクトを取得する"""
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    return conn

# ファイル名からテーブル名を推測する関数
def get_table_name_from_filename(filename):
    """ファイル名から対応するテーブル名を返す"""
    if 'producer' in filename.lower():
        return 'producer_table'
    if 'customer' in filename.lower():
        return 'customer_table'
    if 'item' in filename.lower():
        return 'item_table'
    if 'order_detail' in filename.lower():
        return 'order_detail_table'
    if 'order' in filename.lower():
        return 'order_table'
    return None

def main():
    st.title("CSVデータアップローダー")
    st.markdown("CSVファイルをアップロードして、データベースに挿入します。")

    # ファイルアップローダー
    uploaded_file = st.file_uploader("CSVファイルをアップロードしてください", type="csv")

    if uploaded_file is not None:
        # ファイル名からテーブル名を判別
        table_name = get_table_name_from_filename(uploaded_file.name)

        if table_name:
            st.info(f"ファイル名 `{uploaded_file.name}` からテーブル名 `{table_name}` を推測しました。")
            
            # データフレームとして読み込み
            try:
                df = pd.read_csv(uploaded_file)
                st.write("---")
                st.subheader("アップロードされたデータのプレビュー")
                st.dataframe(df.head())

                if st.button("データベースに挿入"):
                    conn = get_db_connection()
                    try:
                        # データをテーブルに挿入
                        df.to_sql(table_name, conn, if_exists='append', index=False)
                        conn.commit()
                        st.success(f"データが `{table_name}` に正常に挿入されました！")
                    except Exception as e:
                        conn.rollback()
                        st.error(f"データの挿入中にエラーが発生しました: {e}")
                    finally:
                        conn.close()
            except Exception as e:
                st.error(f"CSVファイルの読み込み中にエラーが発生しました: {e}")
        else:
            st.warning("ファイル名から挿入先のテーブルを特定できませんでした。")
            st.markdown("ファイル名には `producer`, `customer`, `item`, `order_detail`, `order` のいずれかを含めてください。")
            
if __name__ == "__main__":
    main()