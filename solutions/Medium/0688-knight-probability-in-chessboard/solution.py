# ──────────────────────────────────────────────────
# Problem  : 688. Knight Probability in Chessboard
# Difficulty: Medium
# Tags     : Dynamic Programming
# Link     : https://leetcode.com/problems/knight-probability-in-chessboard/
# Runtime  : 74 ms (beats 94%)
# Memory   : 19620000 (beats 70%)
# Language : python3
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        # All 8 possible moves for a knight
        moves = [
            (-2, -1), (-2, 1), (-1, -2), (-1, 2),
            (1, -2), (1, 2), (2, -1), (2, 1)
        ]
        
        # dp[r][c] represents the probability of the knight being on cell (r, c)
        dp = [[0.0] * n for _ in range(n)]
        dp[row][column] = 1.0
        
        for _ in range(k):
            next_dp = [[0.0] * n for _ in range(n)]
            for r in range(n):
                for c in range(n):
                    if dp[r][c] > 0:
                        for dr, dc in moves:
                            nr, nc = r + dr, c + dc
                            if 0 <= nr < n and 0 <= nc < n:
                                next_dp[nr][nc] += dp[r][c] / 8.0
            dp = next_dp
            
        # Sum all probabilities of remaining on the board after k moves
        return sum(sum(row_vals) for row_vals in dp)