-- Funnel Analysis: Count orders at each stage
-- Stages: Created -> Approved -> Delivered

SELECT 
    '1. Order Placed' as stage,
    COUNT(order_id) as count,
    0 as drop_off
FROM orders

UNION ALL

SELECT 
    '2. Order Approved' as stage,
    COUNT(order_id) as count,
    (SELECT COUNT(*) FROM orders) - COUNT(order_id) as drop_off
FROM orders
WHERE order_approved_at IS NOT NULL

UNION ALL

SELECT 
    '3. Order Delivered' as stage,
    COUNT(order_id) as count,
    (SELECT COUNT(*) FROM orders WHERE order_approved_at IS NOT NULL) - COUNT(order_id) as drop_off
FROM orders
WHERE order_status = 'delivered';

-- Revenue and AOV Analysis
SELECT 
    COUNT(DISTINCT o.order_id) as total_orders,
    SUM(oi.price) as total_revenue,
    SUM(oi.price) / COUNT(DISTINCT o.order_id) as aov
FROM orders o
JOIN order_items oi ON o.order_id = oi.order_id
WHERE o.order_status = 'delivered';
