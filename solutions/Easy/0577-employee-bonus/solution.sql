-- ──────────────────────────────────────────────────
-- Problem  : 577. Employee Bonus
-- Difficulty: Easy
-- Tags     : Database
-- Link     : https://leetcode.com/problems/employee-bonus/
-- Runtime  : 1553 ms (beats 8%)
-- Memory   : 0B (beats 100%)
-- Language : mysql
-- Copyright: (c) 2026 gayathri16006. All rights reserved.
-- Synced by: leetie
-- ──────────────────────────────────────────────────

SELECT 
    e.name, 
    b.bonus
FROM 
    Employee AS e
LEFT JOIN 
    Bonus AS b
  ON e.empId = b.empId
WHERE 
    b.bonus < 1000 
    OR b.bonus IS NULL;