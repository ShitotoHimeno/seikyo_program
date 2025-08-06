import sqlite3
import pandas as pd

class SQLiteTemplate:
    def __init__(self, db_name='seikyo_db.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def execute(self, query_text):
        self.cursor.execute(query_text)
        self.conn.commit()

    def fetch_dataframe(self, query_text):
        return pd.read_sql_query(query_text, self.conn)

    def close(self):
        self.conn.close()
        
    def commit(self):
        self.conn.commit()