-- ──────────────────────────────────────────────────
-- Problem  : 586. Customer Placing the Largest Number of Orders
-- Difficulty: Easy
-- Tags     : Database
-- Link     : https://leetcode.com/problems/customer-placing-the-largest-number-of-orders/
-- Runtime  : 87 ms (beats 0%)
-- Memory   : 0B (beats 0%)
-- Language : mysql
-- Copyright: (c) 2026 gayathri16006. All rights reserved.
-- Synced by: leetie
-- ──────────────────────────────────────────────────

SELECT 
    customer_number
FROM 
    Orders
GROUP BY 
    customer_number
ORDER BY 
    COUNT(order_number) DESC
LIMIT 1;