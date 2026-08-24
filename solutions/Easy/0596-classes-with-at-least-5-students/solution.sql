-- ──────────────────────────────────────────────────
-- Problem  : 596. Classes With at Least 5 Students
-- Difficulty: Easy
-- Tags     : Database
-- Link     : https://leetcode.com/problems/classes-with-at-least-5-students/
-- Runtime  : 73 ms (beats 0%)
-- Memory   : 0B (beats 0%)
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