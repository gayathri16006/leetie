-- ──────────────────────────────────────────────────
-- Problem  : 550. Game Play Analysis IV
-- Difficulty: Medium
-- Tags     : Database
-- Link     : https://leetcode.com/problems/game-play-analysis-iv/
-- Runtime  : 69 ms (beats 0%)
-- Memory   : 0B (beats 0%)
-- Language : mysql
-- Copyright: (c) 2026 gayathri16006. All rights reserved.
-- Synced by: leetie
-- ──────────────────────────────────────────────────

SELECT 
    ROUND(
        COUNT(a.player_id) / (SELECT COUNT(DISTINCT player_id) FROM Activity), 
        2
    ) AS fraction
FROM (
    SELECT 
        player_id, 
        MIN(event_date) AS first_login
    FROM 
        Activity
    GROUP BY 
        player_id
) first_days
JOIN Activity a
  ON first_days.player_id = a.player_id
 AND a.event_date = DATE_ADD(first_days.first_login, INTERVAL 1 DAY);