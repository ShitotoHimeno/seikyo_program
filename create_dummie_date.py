import pandas as pd
from datetime import datetime, timedelta
import random

# 生産者データ
producers = pd.DataFrame({
    "producer_name": [f"Producer_{i}" for i in range(1, 11)],
    "created_date": [datetime.today().date() - timedelta(days=i*30) for i in range(10)],
    "cancel_date": [None if i % 2 == 0 else (datetime.today().date() - timedelta(days=i*15)) for i in range(10)],
    "update_date": [datetime.today().date()] * 10
})
producers.to_csv("producers.csv", index=False)

# 顧客データ
customers = pd.DataFrame({
    "customer_name": [f"Customer_{i}" for i in range(1, 11)],
    "created_date": [datetime.today().date() - timedelta(days=i*25) for i in range(10)],
    "cancel_date": [None if i % 3 == 0 else (datetime.today().date() - timedelta(days=i*10)) for i in range(10)],
    "area": [random.randint(1, 5) for _ in range(10)],
    "update_date": [datetime.today().date()] * 10
})
customers.to_csv("customers.csv", index=False)

# 商品データ（生産者に紐付け）
items = pd.DataFrame({
    "item_name": [f"Item_{i}" for i in range(1, 11)],
    "item_category": [random.choice(["Fruit", "Vegetable", "Grain"]) for _ in range(10)],
    "price": [random.randint(100, 1000) for _ in range(10)],
    "created_date": [datetime.today().date() - timedelta(days=i*10) for i in range(10)],
    "update_date": [datetime.today().date()] * 10,
    "producer_id": [i % 10 + 1 for i in range(10)]
})
items.to_csv("items.csv", index=False)

# 注文データ（顧客に紐付け）
orders = pd.DataFrame({
    "order_date": [datetime.today().date() - timedelta(days=i*5) for i in range(10)],
    "order_status": [random.choice(["received", "shipped", "cancelled"]) for _ in range(10)],
    "update_date": [datetime.today().date()] * 10,
    "customer_id": [i % 10 + 1 for i in range(10)]
})
orders.to_csv("orders.csv", index=False)

order_details = pd.DataFrame({
    
})
