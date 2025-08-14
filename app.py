import streamlit as st
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

# --- データベース設定 ---
# データベースパスは相対パスが推奨されます
DB_PATH = 'seikyo_db.db'
# データベース接続関数
def get_db_connection():
    """データベース接続オブジェクトを取得する"""
    conn = sqlite3.connect(DB_PATH)
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

# --- Streamlitのメイン処理 ---
def main():
    st.title("生協データ管理ダッシュボード")

    # サイドバーに機能選択ボタンを配置
    st.sidebar.title("機能選択")
    page = st.sidebar.radio("表示するページを選んでください:", ["日別売上推移グラフ", "CSVデータアップロード"])

    if page == "日別売上推移グラフ":
        display_sales_chart()
    elif page == "CSVデータアップロード":
        display_csv_uploader()

def display_sales_chart():
    """日別売上推移グラフを表示するページ"""
    st.header("日別売上金額の推移")
    
    try:
        conn = get_db_connection()
        query = """
        SELECT
            d.order_detail_id,
            d.order_id,
            d.item_id,
            d.quantity,
            o.order_date,
            i.item_name,
            i.price
        FROM
            order_detail_table d
            JOIN order_table o ON d.order_id = o.order_id
            JOIN item_table i ON d.item_id = i.item_id
        """
        order_detail_table = pd.read_sql_query(query, conn)
        conn.close()

        # データ加工と集計
        order_detail_table["order_date"] = pd.to_datetime(order_detail_table["order_date"])
        order_detail_table["money"] = order_detail_table["quantity"] * order_detail_table["price"]
        money_sum_by_date = order_detail_table.groupby("order_date")["money"].sum().reset_index()

        # Matplotlibの日本語フォント設定
        if os.name == 'nt':  # Windowsの場合
            font_path = fm.findfont(fm.FontProperties(family='Yu Gothic'))
            if font_path:
                plt.rcParams['font.family'] = 'Yu Gothic'
            else:
                st.warning("Windows用のフォント（Yu Gothic, Meiryo）が見つかりませんでした。表示に問題があるかもしれません。")
        else: # それ以外のOSの場合 (Mac, Linuxなど)
            plt.rcParams['font.family'] = 'IPAexGothic'
            
        plt.rcParams['axes.unicode_minus'] = False

        # グラフの作成
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(money_sum_by_date["order_date"], money_sum_by_date["money"], marker='o', label="日別売上")
        ax.set_title("日別売上金額の推移")
        ax.set_xlabel("注文日")
        ax.set_ylabel("売上金額")
        ax.legend()
        ax.grid(True)

        st.pyplot(fig)

    except Exception as e:
        st.error(f"データベースの読み込みまたはグラフの作成中にエラーが発生しました: {e}")
        st.info("データベースにデータが存在しない可能性があります。CSVアップローダーからデータを追加してください。")


def display_csv_uploader():
    """CSVデータをアップロードしてデータベースに挿入するページ"""
    st.header("CSVデータアップロード")
    st.markdown("CSVファイルをアップロードして、データベースに挿入します。")

    uploaded_file = st.file_uploader("CSVファイルをアップロードしてください", type="csv")

    if uploaded_file is not None:
        table_name = get_table_name_from_filename(uploaded_file.name)

        if table_name:
            st.info(f"ファイル名 `{uploaded_file.name}` からテーブル名 `{table_name}` を推測しました。")
            try:
                df = pd.read_csv(uploaded_file)
                st.write("---")
                st.subheader("アップロードされたデータのプレビュー")
                st.dataframe(df.head())

                if st.button("データベースに挿入"):
                    conn = get_db_connection()
                    try:
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