import sqlite3

def connect_db():
    return sqlite3.connect("retail.db")

def create_table():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS store_audit (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        store_id TEXT,
        product TEXT,
        stock INTEGER,
        visibility_score INTEGER,
        timestamp TEXT
    )
    """)

    conn.commit()
    conn.close()

def insert_data(data):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO store_audit (store_id, product, stock, visibility_score, timestamp)
    VALUES (?, ?, ?, ?, ?)
    """, (
        data["store_id"],
        data["product"],
        data["stock"],
        data["visibility_score"],
        data["timestamp"]
    ))

    conn.commit()
    conn.close()


def fetch_all_data():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT store_id, product, stock, visibility_score, timestamp FROM store_audit")
    rows = cursor.fetchall()

    conn.close()
    return rows
