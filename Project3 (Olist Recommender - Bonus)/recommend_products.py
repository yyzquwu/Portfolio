import pandas as pd
import numpy as np
import sqlite3
import argparse
from sklearn.decomposition import TruncatedSVD
from scipy.sparse import csr_matrix
import sys
import os

def get_recommendations(product_id, db_path='../Project1 (DA)/olist.db', n_recommendations=5):
    # 1. Load Data
    if not os.path.exists(db_path):
        print(f"Error: Database not found at {db_path}")
        return

    conn = sqlite3.connect(db_path)
    query = """
    SELECT 
        c.customer_unique_id,
        oi.product_id,
        COUNT(oi.order_id) as purchase_count
    FROM orders o
    JOIN order_items oi ON o.order_id = oi.order_id
    JOIN customers c ON o.customer_id = c.customer_id
    GROUP BY c.customer_unique_id, oi.product_id
    """
    df = pd.read_sql(query, conn)
    
    # Load product names for display
    products_df = pd.read_sql("SELECT product_id, product_category_name FROM products", conn)
    conn.close()

    # 2. Filter Data (Min 5 purchases)
    min_purchases = 5
    product_counts = df.groupby('product_id')['purchase_count'].sum()
    active_products = product_counts[product_counts >= min_purchases].index
    df_filtered = df[df['product_id'].isin(active_products)]

    if product_id not in active_products:
        print(f"Product {product_id} not found or has insufficient data.")
        return

    # 3. Build Matrix
    user_ids = df_filtered['customer_unique_id'].unique()
    product_ids = df_filtered['product_id'].unique()

    product_to_idx = {product: i for i, product in enumerate(product_ids)}
    idx_to_product = {i: product for product, i in product_to_idx.items()}

    rows = df_filtered['customer_unique_id'].map({user: i for i, user in enumerate(user_ids)})
    cols = df_filtered['product_id'].map(product_to_idx)
    values = df_filtered['purchase_count']

    matrix = csr_matrix((values, (rows, cols)), shape=(len(user_ids), len(product_ids)))

    # 4. Train SVD
    svd = TruncatedSVD(n_components=20, random_state=42)
    matrix_reduced = svd.fit_transform(matrix)
    corr_matrix = np.corrcoef(svd.components_.T)

    # 5. Get Recommendations
    product_idx = product_to_idx[product_id]
    correlation_product_id = corr_matrix[product_idx]
    recommend_indices = correlation_product_id.argsort()[-n_recommendations-1:-1][::-1]

    print(f"\n--- Recommendations for Product: {product_id} ---")
    category = products_df[products_df['product_id'] == product_id]['product_category_name'].values[0]
    print(f"Category: {category}\n")
    
    print("Top Recommended Products:")
    for i, idx in enumerate(recommend_indices):
        rec_id = idx_to_product[idx]
        rec_cat = products_df[products_df['product_id'] == rec_id]['product_category_name'].values[0]
        print(f"{i+1}. {rec_id} ({rec_cat})")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Product Recommendation Engine')
    parser.add_argument('product_id', type=str, help='Product ID to get recommendations for')
    args = parser.parse_args()

    get_recommendations(args.product_id)
