-- 📊 Sales Trend Analysis SQL Script

-- 1️⃣ Monthly Revenue & Order Volume
SELECT 
    CAST(strftime('%Y', order_date) AS INTEGER) AS year,
    CAST(strftime('%m', order_date) AS INTEGER) AS month,
    COUNT(DISTINCT order_id) AS order_volume,
    ROUND(SUM(amount), 2) AS total_revenue
FROM online_sales
WHERE amount IS NOT NULL
GROUP BY year, month
ORDER BY year, month;

-- 2️⃣ Top 3 Months by Revenue
SELECT
CAST(strftime('%Y', order_date) AS INTEGER) AS year,
CAST(strftime('%m', order_date) AS INTEGER) AS month,
CASE CAST(strftime('%m', order_date) AS INTEGER)
WHEN 1 THEN 'January' WHEN 2 THEN 'February' WHEN 3 THEN 'March'
WHEN 4 THEN 'April' WHEN 5 THEN 'May' WHEN 6 THEN 'June'
WHEN 7 THEN 'July' WHEN 8 THEN 'August' WHEN 9 THEN 'September'
WHEN 10 THEN 'October' WHEN 11 THEN 'November' WHEN 12 THEN 'December'
END AS month_name,
ROUND(SUM(amount), 2) AS total_revenue,
COUNT(DISTINCT order_id) AS order_count
FROM online_sales
WHERE amount IS NOT NULL
GROUP BY
CAST(strftime('%Y', order_date) AS INTEGER),
CAST(strftime('%m', order_date) AS INTEGER)
ORDER BY total_revenue DESC
LIMIT 3;
-- 3️⃣ Product Category Performance
SELECT
    product_category,
    COUNT(DISTINCT order_id) AS orders,
    ROUND(SUM(amount), 2) AS revenue,
    ROUND(AVG(amount), 2) AS avg_order_value
FROM online_sales
WHERE amount IS NOT NULL
GROUP BY product_category
ORDER BY revenue DESC;
