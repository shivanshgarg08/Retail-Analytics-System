from fastapi import FastAPI
import pandas as pd
import sqlite3
from database import fetch_all_data

try:
    from database import create_table as _create_table
except ImportError:
    _create_table = None

try:
    from database import insert_data as _insert_data
except ImportError:
    _insert_data = None


def create_table() -> None:
    if _create_table is not None:
        _create_table()
        return

    with sqlite3.connect("retail.db") as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS store_audit (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                store_id TEXT,
                product TEXT,
                stock INTEGER,
                visibility_score INTEGER,
                timestamp TEXT
            )
            """
        )
        conn.commit()


def insert_data(data: dict) -> None:
    if _insert_data is not None:
        _insert_data(data)
        return

    with sqlite3.connect("retail.db") as conn:
        conn.execute(
            """
            INSERT INTO store_audit (store_id, product, stock, visibility_score, timestamp)
            VALUES (?, ?, ?, ?, ?)
            """,
            (
                data.get("store_id"),
                data.get("product"),
                data.get("stock"),
                data.get("visibility_score"),
                data.get("timestamp"),
            ),
        )
        conn.commit()

app = FastAPI()

create_table()

@app.get("/")
def home():
    return {"message": "Retail Audit API running"}

@app.post("/store-audit")
def add_audit(data: dict):
    insert_data(data)
    return {"status": "Data inserted"}


@app.get("/reports")
def get_reports():
    data = fetch_all_data()

    df = pd.DataFrame(data, columns=["store_id", "product", "stock", "visibility_score", "timestamp"])

    if df.empty:
        return {"status": "No data available"}

    low_stock = df[df["stock"] < 10]
    avg_visibility = round(df["visibility_score"].mean(), 2)
    store_stock = df.groupby("store_id")["stock"].sum().to_dict()

    return {
        "status": "success",
        "insights": {
            "low_stock_count": len(low_stock),
            "low_stock_items": low_stock.to_dict(orient="records"),
            "average_visibility_score": avg_visibility,
            "store_stock_distribution": store_stock,
        },
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)