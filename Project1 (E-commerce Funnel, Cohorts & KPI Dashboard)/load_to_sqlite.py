import pandas as pd
import sqlite3
import os
import glob

# Path where the data was downloaded
DATA_PATH = "/home/yeqiu/.cache/kagglehub/datasets/olistbr/brazilian-ecommerce/versions/2"
DB_NAME = "olist.db"

def load_to_sqlite():
    print(f"Loading data from {DATA_PATH} into {DB_NAME}...")
    
    # Connect to SQLite database (creates it if it doesn't exist)
    conn = sqlite3.connect(DB_NAME)
    
    # Get all CSV files
    csv_files = glob.glob(os.path.join(DATA_PATH, "*.csv"))
    
    if not csv_files:
        print("No CSV files found!")
        return

    for file_path in csv_files:
        file_name = os.path.basename(file_path)
        # Create table name: remove extension and 'olist_' prefix for cleaner names
        table_name = file_name.replace(".csv", "").replace("olist_", "").replace("_dataset", "")
        
        print(f"Processing {file_name} -> table: {table_name}")
        
        try:
            df = pd.read_csv(file_path)
            # Write to SQLite
            df.to_sql(table_name, conn, if_exists="replace", index=False)
            print(f"  - Loaded {len(df)} rows.")
        except Exception as e:
            print(f"  - Error loading {file_name}: {e}")
            
            
    # Create indices for performance
    print("\nCreating indices...")
    try:
        conn.execute("CREATE INDEX IF NOT EXISTS idx_orders_order_id ON orders(order_id)")
        conn.execute("CREATE INDEX IF NOT EXISTS idx_orders_status ON orders(order_status)")
        conn.execute("CREATE INDEX IF NOT EXISTS idx_order_items_order_id ON order_items(order_id)")
        print("  - Indices created successfully.")
    except Exception as e:
        print(f"  - Error creating indices: {e}")

    conn.close()
    print(f"\nSuccessfully created {DB_NAME} with tables.")

if __name__ == "__main__":
    load_to_sqlite()
