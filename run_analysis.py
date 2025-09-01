import sqlite3
import pandas as pd

with sqlite3.connect('sales_analysis.db') as conn:
    print("\n📊 TOP 3 MONTHS BY REVENUE")
    q1 = """
    SELECT 
        strftime('%Y', order_date) AS year,
        strftime('%m', order_date) AS month,
        ROUND(SUM(amount), 2) AS total_revenue
    FROM online_sales
    WHERE amount IS NOT NULL
    GROUP BY year, month
    ORDER BY total_revenue DESC
    LIMIT 3;
    """
    print(pd.read_sql_query(q1, conn))

    print("\n📊 CATEGORY PERFORMANCE")
    q2 = """
    SELECT product_category, COUNT(DISTINCT order_id) AS orders, ROUND(SUM(amount), 2) AS revenue
    FROM online_sales
    WHERE amount IS NOT NULL
    GROUP BY product_category
    ORDER BY revenue DESC;
    """
    print(pd.read_sql_query(q2, conn))
