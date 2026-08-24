-- ──────────────────────────────────────────────────
-- Problem  : 610. Triangle Judgement
-- Difficulty: Easy
-- Tags     : Database
-- Link     : https://leetcode.com/problems/triangle-judgement/
-- Runtime  : 308 ms (beats 62%)
-- Memory   : 0B (beats 100%)
-- Language : mysql
-- Copyright: (c) 2026 gayathri16006. All rights reserved.
-- Synced by: leetie
-- ──────────────────────────────────────────────────

SELECT 
    x,
    y,
    z,
    CASE 
        WHEN x + y > z AND x + z > y AND y + z > x THEN 'Yes'
        ELSE 'No'
    END AS triangle
FROM Triangle;