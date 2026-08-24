-- ──────────────────────────────────────────────────
-- Problem  : 584. Find Customer Referee
-- Difficulty: Easy
-- Tags     : Database
-- Link     : https://leetcode.com/problems/find-customer-referee/
-- Runtime  : 516 ms (beats 59%)
-- Memory   : 0B (beats 100%)
-- Language : mysql
-- Copyright: (c) 2026 gayathri16006. All rights reserved.
-- Synced by: leetie
-- ──────────────────────────────────────────────────

SELECT 
    name
FROM 
    Customer
WHERE 
    referee_id != 2 
    OR referee_id IS NULL;