-- ──────────────────────────────────────────────────
-- Problem  : 602. Friend Requests II: Who Has the Most Friends
-- Difficulty: Medium
-- Tags     : Database
-- Link     : https://leetcode.com/problems/friend-requests-ii-who-has-the-most-friends/
-- Runtime  : 74 ms (beats 0%)
-- Memory   : 0B (beats 0%)
-- Language : mysql
-- Copyright: (c) 2026 gayathri16006. All rights reserved.
-- Synced by: leetie
-- ──────────────────────────────────────────────────

WITH AllFriends AS (
    SELECT requester_id AS id FROM RequestAccepted
    UNION ALL
    SELECT accepter_id AS id FROM RequestAccepted
)
SELECT 
    id, 
    COUNT(*) AS num
FROM 
    AllFriends
GROUP BY 
    id
ORDER BY 
    num DESC
LIMIT 1;