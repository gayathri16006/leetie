-- ──────────────────────────────────────────────────
-- Problem  : 596. Classes With at Least 5 Students
-- Difficulty: Easy
-- Tags     : Database
-- Link     : https://leetcode.com/problems/classes-with-at-least-5-students/
-- Runtime  : 636 ms (beats 5%)
-- Memory   : 0B (beats 100%)
-- Language : mysql
-- Copyright: (c) 2026 gayathri16006. All rights reserved.
-- Synced by: leetie
-- ──────────────────────────────────────────────────

SELECT 
    class
FROM 
    Courses
GROUP BY 
    class
HAVING 
    COUNT(student) >= 5;