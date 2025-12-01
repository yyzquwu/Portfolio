-- 1. Get first purchase month for each customer (Cohort)
WITH first_purchase AS (
    SELECT 
        c.customer_unique_id,
        MIN(DATE(o.order_purchase_timestamp, 'start of month')) as cohort_month
    FROM orders o
    JOIN customers c ON o.customer_id = c.customer_id
    WHERE o.order_status = 'delivered'
    GROUP BY 1
),

-- 2. Get all purchase months for each customer
customer_activities AS (
    SELECT 
        c.customer_unique_id,
        DATE(o.order_purchase_timestamp, 'start of month') as activity_month
    FROM orders o
    JOIN customers c ON o.customer_id = c.customer_id
    WHERE o.order_status = 'delivered'
),

-- 3. Join to calculate month difference
cohort_activities AS (
    SELECT 
        fp.cohort_month,
        ca.activity_month,
        -- Calculate month difference: (YearDiff * 12) + MonthDiff
        (CAST(STRFTIME('%Y', ca.activity_month) AS INTEGER) - CAST(STRFTIME('%Y', fp.cohort_month) AS INTEGER)) * 12 +
        (CAST(STRFTIME('%m', ca.activity_month) AS INTEGER) - CAST(STRFTIME('%m', fp.cohort_month) AS INTEGER)) as month_diff,
        COUNT(DISTINCT fp.customer_unique_id) as active_customers
    FROM first_purchase fp
    JOIN customer_activities ca ON fp.customer_unique_id = ca.customer_unique_id
    GROUP BY 1, 2
)

-- 4. Final Result
SELECT 
    cohort_month,
    month_diff,
    active_customers
FROM cohort_activities
ORDER BY 1, 2;
