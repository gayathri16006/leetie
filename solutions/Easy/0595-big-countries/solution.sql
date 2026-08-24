-- ──────────────────────────────────────────────────
-- Problem  : 595. Big Countries
-- Difficulty: Easy
-- Tags     : Database
-- Link     : https://leetcode.com/problems/big-countries/
-- Runtime  : 377 ms (beats 15%)
-- Memory   : 0B (beats 100%)
-- Language : mysql
-- Copyright: (c) 2026 gayathri16006. All rights reserved.
-- Synced by: leetie
-- ──────────────────────────────────────────────────

SELECT 
    name, 
    population, 
    area
FROM 
    World
WHERE 
    area >= 3000000 
    OR population >= 25000000;