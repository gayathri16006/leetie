-- ──────────────────────────────────────────────────
-- Problem  : 620. Not Boring Movies
-- Difficulty: Easy
-- Tags     : Database
-- Link     : https://leetcode.com/problems/not-boring-movies/
-- Runtime  : 71 ms (beats 0%)
-- Memory   : 0B (beats 0%)
-- Language : mysql
-- Copyright: (c) 2026 gayathri16006. All rights reserved.
-- Synced by: leetie
-- ──────────────────────────────────────────────────

SELECT id, movie, description, rating
FROM Cinema
WHERE id % 2 = 1
  AND description <> 'boring'
ORDER BY rating DESC;