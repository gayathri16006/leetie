-- ──────────────────────────────────────────────────
-- Problem  : 627. Swap Sex of Employees
-- Difficulty: Easy
-- Tags     : Database
-- Link     : https://leetcode.com/problems/swap-sex-of-employees/
-- Runtime  : 267 ms (beats 57%)
-- Memory   : 0B (beats 100%)
-- Language : mysql
-- Copyright: (c) 2026 gayathri16006. All rights reserved.
-- Synced by: leetie
-- ──────────────────────────────────────────────────

UPDATE Salary
SET sex = CASE 
    WHEN sex = 'm' THEN 'f' 
    ELSE 'm' 
END;