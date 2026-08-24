-- ──────────────────────────────────────────────────
-- Problem  : 626. Exchange Seats
-- Difficulty: Medium
-- Tags     : Database
-- Link     : https://leetcode.com/problems/exchange-seats/
-- Runtime  : 1092 ms (beats 5%)
-- Memory   : 0B (beats 100%)
-- Language : mysql
-- Copyright: (c) 2026 gayathri16006. All rights reserved.
-- Synced by: leetie
-- ──────────────────────────────────────────────────

SELECT 
    CASE 
        -- If odd and is the last row, keep id as is
        WHEN id % 2 = 1 AND id = (SELECT COUNT(*) FROM Seat) THEN id
        -- If odd, pair with the next student
        WHEN id % 2 = 1 THEN id + 1
        -- If even, pair with the previous student
        ELSE id - 1
    END AS id,
    student
FROM Seat
ORDER BY id ASC;