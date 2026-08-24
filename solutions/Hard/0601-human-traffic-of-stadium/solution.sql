-- ──────────────────────────────────────────────────
-- Problem  : 601. Human Traffic of Stadium
-- Difficulty: Hard
-- Tags     : Database
-- Link     : https://leetcode.com/problems/human-traffic-of-stadium/
-- Runtime  : 411 ms (beats 49%)
-- Memory   : 0B (beats 100%)
-- Language : mysql
-- Copyright: (c) 2026 gayathri16006. All rights reserved.
-- Synced by: leetie
-- ──────────────────────────────────────────────────

WITH HighTraffic AS (
    SELECT 
        id,
        visit_date,
        people,
        id - ROW_NUMBER() OVER (ORDER BY id) AS grp
    FROM 
        Stadium
    WHERE 
        people >= 100
),
GroupCounts AS (
    SELECT 
        id,
        visit_date,
        people,
        COUNT(*) OVER (PARTITION BY grp) AS grp_count
    FROM 
        HighTraffic
)
SELECT 
    id, 
    visit_date, 
    people
FROM 
    GroupCounts
WHERE 
    grp_count >= 3
ORDER BY 
    visit_date ASC;