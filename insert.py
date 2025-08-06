import sqlite3
import pandas as pd

from sqlite import SQLiteTemplate

sql = SQLiteTemplate()
customers_df = pd.read_csv('customers.csv')
items_df = pd.read_csv('items.csv')
orders_df = pd.read_csv('orders.csv')



sql.execute('''
    INSERT 
'''
)

print("これは試験です")