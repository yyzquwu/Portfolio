import sqlite3

db_path = '/home/yeqiu/dev/Portfolio/Project1 (E-commerce Funnel, Cohorts & KPI Dashboard)/olist.db'
conn = sqlite3.connect(db_path)

indexes = [
    "CREATE INDEX IF NOT EXISTS idx_orders_status            ON orders(order_status);",
    "CREATE INDEX IF NOT EXISTS idx_orders_delivered         ON orders(order_delivered_customer_date);",
    "CREATE INDEX IF NOT EXISTS idx_orders_customer          ON orders(customer_id);",
    "CREATE INDEX IF NOT EXISTS idx_orders_purchase_date     ON orders(order_purchase_timestamp);",
    "CREATE INDEX IF NOT EXISTS idx_reviews_order            ON order_reviews(order_id);",
    "CREATE INDEX IF NOT EXISTS idx_payments_order           ON order_payments(order_id);",
    "CREATE INDEX IF NOT EXISTS idx_items_order               ON order_items(order_id);",
    "CREATE INDEX IF NOT EXISTS idx_customers_id              ON customers(customer_id);",
]

for idx in indexes:
    conn.execute(idx)

conn.close()
