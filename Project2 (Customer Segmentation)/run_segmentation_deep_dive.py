import pandas as pd
import numpy as np
import sqlite3
import matplotlib.pyplot as plt
import seaborn as sns

# Connect to the SQLite database
db_path = '/home/yeqiu/dev/Portfolio/Project1 (E-commerce Funnel, Cohorts & KPI Dashboard)/olist.db'
conn = sqlite3.connect(db_path)
print(f"Connected to database at: {db_path}")

# --- 1. Re-create RFM Segments (Simplified for Script) ---
print("\n--- Calculating RFM Segments ---")
query_rfm = """
SELECT 
    o.customer_id,
    c.customer_unique_id,
    o.order_purchase_timestamp,
    p.payment_value
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
JOIN order_payments p ON o.order_id = p.order_id
WHERE o.order_status = 'delivered'
"""
df_rfm = pd.read_sql(query_rfm, conn)
df_rfm['order_purchase_timestamp'] = pd.to_datetime(df_rfm['order_purchase_timestamp'])

# Reference date (max date + 1 day)
max_date = df_rfm['order_purchase_timestamp'].max() + pd.Timedelta(days=1)

# Calculate RFM
rfm = df_rfm.groupby('customer_unique_id').agg({
    'order_purchase_timestamp': lambda x: (max_date - x.max()).days, # Recency
    'customer_id': 'count', # Frequency (count of orders/payments)
    'payment_value': 'sum' # Monetary
}).reset_index()

rfm.columns = ['customer_unique_id', 'Recency', 'Frequency', 'Monetary']

# Scoring (Quintiles)
rfm['R_Score'] = pd.qcut(rfm['Recency'], 5, labels=[5, 4, 3, 2, 1])
# Frequency is skewed, use custom bins or rank method 'first'
rfm['F_Score'] = pd.qcut(rfm['Frequency'].rank(method='first'), 5, labels=[1, 2, 3, 4, 5])
rfm['M_Score'] = pd.qcut(rfm['Monetary'], 5, labels=[1, 2, 3, 4, 5])

# Convert to string
rfm['RFM_Score'] = rfm['R_Score'].astype(str) + rfm['F_Score'].astype(str)

# Segment Logic
def segment_customer(row):
    r = int(row['R_Score'])
    f = int(row['F_Score'])
    
    if r >= 4 and f >= 4: return 'Champions'
    elif r >= 3 and f >= 3: return 'Loyal Customers'
    elif r >= 4 and f == 1: return 'Recent Users'
    elif r <= 2 and f >= 4: return 'Can\'t Lose Them'
    elif r <= 2 and f <= 2: return 'Hibernating'
    else: return 'Others'

rfm['Segment'] = rfm.apply(segment_customer, axis=1)
print("Segments created.")
print(rfm['Segment'].value_counts())

# --- 2. Deep Dive: Product Preferences by Segment ---
print("\n--- Deep Dive: Product Categories by Segment ---")
# We need to join RFM back to Orders -> Items -> Products
# This is heavy, so let's do it in steps or a smart query
# First, map customer_unique_id to segment
segment_map = rfm[['customer_unique_id', 'Segment']]

# Get products purchased by each customer
query_products = """
SELECT 
    c.customer_unique_id,
    pr.product_category_name
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
JOIN order_items oi ON o.order_id = oi.order_id
JOIN products pr ON oi.product_id = pr.product_id
"""
df_prods = pd.read_sql(query_products, conn)

# Merge
df_seg_prods = df_prods.merge(segment_map, on='customer_unique_id', how='inner')

# Top category per segment
for segment in rfm['Segment'].unique():
    print(f"\nTop 3 Categories for {segment}:")
    top_cats = df_seg_prods[df_seg_prods['Segment'] == segment]['product_category_name'].value_counts().head(3)
    print(top_cats)

# --- 3. Deep Dive: Review Scores by Segment ---
print("\n--- Deep Dive: Review Scores by Segment ---")
query_reviews = """
SELECT 
    c.customer_unique_id,
    r.review_score
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
JOIN order_reviews r ON o.order_id = r.order_id
"""
df_reviews = pd.read_sql(query_reviews, conn)
df_seg_reviews = df_reviews.merge(segment_map, on='customer_unique_id', how='inner')

print("\nAverage Review Score per Segment:")
print(df_seg_reviews.groupby('Segment')['review_score'].mean().sort_values(ascending=False))

conn.close()
