import sqlite3
import pandas as pd

from sqlite import SQLiteTemplate

sql = SQLiteTemplate()

# producer_table
sql.execute('''
CREATE TABLE IF NOT EXISTS producer_table (
    producer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    producer_name TEXT NOT NULL,
    created_date DATE NOT NULL,
    cancel_date DATE,
    update_date DATE NOT NULL
)
''')

# customer_table
sql.execute('''
CREATE TABLE IF NOT EXISTS customer_table (
    customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_name TEXT,
    created_date DATE NOT NULL,
    cancel_date DATE,
    area INTEGER,
    update_date DATE NOT NULL
)
''')

# item_table
sql.execute('''
CREATE TABLE IF NOT EXISTS item_table (
    item_id INTEGER PRIMARY KEY AUTOINCREMENT,
    item_name TEXT NOT NULL,
    item_category TEXT,
    price INTEGER NOT NULL,
    created_date DATE NOT NULL,
    update_date DATE NOT NULL,
    producer_id INTEGER NOT NULL,
    FOREIGN KEY (producer_id) REFERENCES producer_table(producer_id)
)
''')

# order_table
sql.execute('''
CREATE TABLE IF NOT EXISTS order_table (
    order_id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_date DATE NOT NULL,
    order_status TEXT,
    update_date DATE NOT NULL,
    customer_id INTEGER NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES customer_table(customer_id)
)
''')

# order_detail_table
sql.execute('''
CREATE TABLE IF NOT EXISTS order_detail_table (
    order_detail_id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id INTEGER NOT NULL,
    item_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    update_date DATE NOT NULL,
    FOREIGN KEY (order_id) REFERENCES order_table(order_id),
    FOREIGN KEY (item_id) REFERENCES item_table(item_id)
)
''')

sql.commit()
sql.close()

print("create_table.pyが実行されました")
