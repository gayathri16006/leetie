-- ──────────────────────────────────────────────────
-- Problem  : 607. Sales Person
-- Difficulty: Easy
-- Tags     : Database
-- Link     : https://leetcode.com/problems/sales-person/
-- Runtime  : 1725 ms (beats 32%)
-- Memory   : 0B (beats 100%)
-- Language : mysql
-- Copyright: (c) 2026 gayathri16006. All rights reserved.
-- Synced by: leetie
-- ──────────────────────────────────────────────────

SELECT name
FROM SalesPerson
WHERE sales_id NOT IN (
    SELECT o.sales_id
    FROM Orders o
    JOIN Company c ON o.com_id = c.com_id
    WHERE c.name = 'RED'
);