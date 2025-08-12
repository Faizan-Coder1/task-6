import sqlite3
import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta
import os

def generate_sample_data():
    random.seed(42)
    np.random.seed(42)

    start_date = datetime(2022, 1, 1)
    end_date = datetime(2024, 12, 31)
    products = {
        'Electronics': (50, 2000),
        'Clothing': (15, 300),
        'Books': (5, 80),
        'Home & Garden': (20, 500),
        'Sports': (10, 800)
    }

    rows = []
    for order_id in range(1, 5051):
        order_date = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))
        category = random.choice(list(products.keys()))
        price = random.uniform(*products[category])
        if random.random() < 0.02:  # NULLs
            amount = None
        else:
            amount = round(price * random.uniform(0.8, 1.2), 2)
        rows.append([order_id, order_date.strftime("%Y-%m-%d"), amount, f"{category[:3].upper()}{random.randint(1,20):03d}", category])

    df = pd.DataFrame(rows, columns=['order_id', 'order_date', 'amount', 'product_id', 'product_category'])
    df.to_csv('online_sales.csv', index=False)
    return df

def create_database():
    if not os.path.exists('online_sales.csv'):
        df = generate_sample_data()
    else:
        df = pd.read_csv('online_sales.csv')

    conn = sqlite3.connect('sales_analysis.db')
    df.to_sql('online_sales', conn, if_exists='replace', index=False)
    conn.close()
    print("✅ Database created: sales_analysis.db")

if __name__ == "__main__":
    create_database()
