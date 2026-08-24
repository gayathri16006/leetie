-- ──────────────────────────────────────────────────
-- Problem  : 619. Biggest Single Number
-- Difficulty: Easy
-- Tags     : Database
-- Link     : https://leetcode.com/problems/biggest-single-number/
-- Runtime  : 569 ms (beats 18%)
-- Memory   : 0B (beats 100%)
-- Language : mysql
-- Copyright: (c) 2026 gayathri16006. All rights reserved.
-- Synced by: leetie
-- ──────────────────────────────────────────────────

SELECT MAX(num) AS num
FROM (
    SELECT num
    FROM MyNumbers
    GROUP BY num
    HAVING COUNT(num) = 1
) AS single_numbers;