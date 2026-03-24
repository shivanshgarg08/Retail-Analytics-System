import streamlit as st
import pandas as pd
import sqlite3

# Load data
conn = sqlite3.connect("retail.db")
df = pd.read_sql_query("SELECT * FROM store_audit", conn)

st.title("📊 Retail Analytics Dashboard")

# 🔹 KPI Metrics
st.subheader("Key Metrics")
col1, col2, col3 = st.columns(3)

col1.metric("Total Records", len(df))
col2.metric("Low Stock Items", len(df[df["stock"] < 10]))
col3.metric("Avg Visibility", round(df["visibility_score"].mean(), 2))

# 🔹 Low Stock
st.subheader("Low Stock Alerts")
low_stock = df[df["stock"] < 10]
st.dataframe(low_stock)

st.subheader("⚠️ Stores Needing Attention")

problem_stores = df[df["stock"] < 10].groupby("store_id").size().sort_values(ascending=False)

st.bar_chart(problem_stores)

# 🔹 Store-wise Stock
st.subheader("Stock by Store")
store_stock = df.groupby("store_id")["stock"].sum()
st.bar_chart(store_stock)

# 🔹 Product Distribution
st.subheader("Product Distribution")
product_counts = df["product"].value_counts()
st.bar_chart(product_counts)

st.subheader("🏆 Best Performing Products")

product_perf = df.groupby("product")["visibility_score"].mean().sort_values(ascending=False)

st.bar_chart(product_perf)