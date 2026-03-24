import random
import sqlite3
from datetime import datetime, timedelta

conn = sqlite3.connect("retail.db")
cursor = conn.cursor()

products = ["Milk", "Bread", "Coke", "Pepsi", "Chips"]
stores = [f"S{i}" for i in range(1, 11)]

for _ in range(200):  # generate 200 records
    store_id = random.choice(stores)
    product = random.choice(products)
    stock = random.randint(1, 50)
    visibility_score = random.randint(1, 10)

    date = datetime.now() - timedelta(days=random.randint(0, 10))

    cursor.execute("""
    INSERT INTO store_audit (store_id, product, stock, visibility_score, timestamp)
    VALUES (?, ?, ?, ?, ?)
    """, (store_id, product, stock, visibility_score, date.strftime("%Y-%m-%d")))

conn.commit()
conn.close()

print("200 records inserted!")