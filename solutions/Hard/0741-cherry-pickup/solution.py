# ──────────────────────────────────────────────────
# Problem  : 741. Cherry Pickup
# Difficulty: Hard
# Tags     : Array, Dynamic Programming, Matrix
# Link     : https://leetcode.com/problems/cherry-pickup/
# Runtime  : 514 ms (beats 26%)
# Memory   : 74580000 (beats 38%)
# Language : python3
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def cherryPickup(self, grid: list[list[int]]) -> int:
        n = len(grid)
        memo = {}

        def dp(r1: int, c1: int, c2: int) -> int:
            r2 = r1 + c1 - c2
            
            # Out of bounds or thorn cell
            if r1 == n or r2 == n or c1 == n or c2 == n or grid[r1][c1] == -1 or grid[r2][c2] == -1:
                return -float('inf')
            
            # Reached bottom-right corner
            if r1 == n - 1 and c1 == n - 1:
                return grid[r1][c1]
            
            if (r1, c1, c2) in memo:
                return memo[(r1, c1, c2)]
            
            # Current cell cherries
            cherries = grid[r1][c1]
            if c1 != c2:
                cherries += grid[r2][c2]
            
            # Both persons can move right (R) or down (D) -> 4 combinations
            max_future = max(
                dp(r1 + 1, c1, c2),      # D, D
                dp(r1 + 1, c1, c2 + 1),  # D, R
                dp(r1, c1 + 1, c2),      # R, D
                dp(r1, c1 + 1, c2 + 1)   # R, R
            )
            
            ans = cherries + max_future
            memo[(r1, c1, c2)] = ans
            return ans

        result = dp(0, 0, 0)
        return max(0, result)