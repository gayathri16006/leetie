-- ──────────────────────────────────────────────────
-- Problem  : 511. Game Play Analysis I
-- Difficulty: Easy
-- Tags     : Database
-- Link     : https://leetcode.com/problems/game-play-analysis-i/
-- Runtime  : 469 ms (beats 93%)
-- Memory   : 0B (beats 100%)
-- Language : mysql
-- Copyright: (c) 2026 gayathri16006. All rights reserved.
-- Synced by: leetie
-- ──────────────────────────────────────────────────

SELECT 
    player_id, 
    MIN(event_date) AS first_login
FROM 
    Activity
GROUP BY 
    player_id;