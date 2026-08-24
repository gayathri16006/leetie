-- ──────────────────────────────────────────────────
-- Problem  : 570. Managers with at Least 5 Direct Reports
-- Difficulty: Medium
-- Tags     : Database
-- Link     : https://leetcode.com/problems/managers-with-at-least-5-direct-reports/
-- Runtime  : 70 ms (beats 0%)
-- Memory   : 0B (beats 0%)
-- Language : mysql
-- Copyright: (c) 2026 gayathri16006. All rights reserved.
-- Synced by: leetie
-- ──────────────────────────────────────────────────

SELECT 
    m.name
FROM 
    Employee AS e
JOIN 
    Employee AS m
  ON e.managerId = m.id
GROUP BY 
    m.id, m.name
HAVING 
    COUNT(e.id) >= 5;