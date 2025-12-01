import pandas as pd
import numpy as np
import sqlite3
import matplotlib.pyplot as plt
import seaborn as sns

# Connect to the SQLite database
db_path = '/home/yeqiu/dev/Portfolio/Project1 (E-commerce Funnel, Cohorts & KPI Dashboard)/olist.db'
conn = sqlite3.connect(db_path)
print(f"Connected to database at: {db_path}")

# 1. Delivery Performance Analysis
print("\n--- 1. Delivery Performance Analysis ---")
query_delivery = """
SELECT 
    o.order_id,
    o.order_purchase_timestamp,
    o.order_delivered_customer_date,
    o.order_estimated_delivery_date,
    r.review_score
FROM orders o
JOIN order_reviews r ON o.order_id = r.order_id
WHERE o.order_status = 'delivered'
  AND o.order_delivered_customer_date IS NOT NULL
"""
df_delivery = pd.read_sql(query_delivery, conn)

# Convert dates
df_delivery['order_purchase_timestamp'] = pd.to_datetime(df_delivery['order_purchase_timestamp'])
df_delivery['order_delivered_customer_date'] = pd.to_datetime(df_delivery['order_delivered_customer_date'])
df_delivery['order_estimated_delivery_date'] = pd.to_datetime(df_delivery['order_estimated_delivery_date'])

# Calculate metrics
df_delivery['delivery_days'] = (df_delivery['order_delivered_customer_date'] - df_delivery['order_purchase_timestamp']).dt.days
df_delivery['delay_days'] = (df_delivery['order_delivered_customer_date'] - df_delivery['order_estimated_delivery_date']).dt.days

print(f"Average Delivery Time: {df_delivery['delivery_days'].mean():.2f} days")
print(f"Average Delay: {df_delivery['delay_days'].mean():.2f} days (Negative means early)")

# Correlation
corr = df_delivery[['delivery_days', 'delay_days', 'review_score']].corr()
print("\nCorrelation Matrix:")
print(corr)

# 2. Payment Analysis
print("\n--- 2. Payment Analysis ---")
query_payments = """
SELECT 
    payment_type,
    payment_installments,
    payment_value
FROM order_payments
"""
df_payments = pd.read_sql(query_payments, conn)

print("\nPayment Type Distribution:")
print(df_payments['payment_type'].value_counts(normalize=True))

print("\nAverage Installments by Payment Type:")
print(df_payments.groupby('payment_type')['payment_installments'].mean())

# 3. Geospatial Analysis
print("\n--- 3. Geospatial Analysis ---")
query_geo = """
SELECT 
    c.customer_state,
    SUM(p.payment_value) as total_revenue,
    COUNT(DISTINCT o.order_id) as total_orders
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
JOIN order_payments p ON o.order_id = p.order_id
GROUP BY c.customer_state
ORDER BY total_revenue DESC
"""
df_geo = pd.read_sql(query_geo, conn)

print("\nTop 5 States by Revenue:")
print(df_geo.head(5))

conn.close()