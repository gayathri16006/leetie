# ──────────────────────────────────────────────────
# Problem  : 764. Largest Plus Sign
# Difficulty: Medium
# Tags     : Array, Dynamic Programming
# Link     : https://leetcode.com/problems/largest-plus-sign/
# Runtime  : 0 ms (beats 0%)
# Memory   : 19416000 (beats 0%)
# Language : python3
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: list[list[int]]) -> int:
        mines_set = {(r, c) for r, c in mines}
        dp = [[0] * n for _ in range(n)]
        
        # Calculate consecutive 1s from all 4 directions
        for r in range(n):
            # Left
            count = 0
            for c in range(n):
                count = 0 if (r, c) in mines_set else count + 1
                dp[r][c] = count
            
            # Right
            count = 0
            for c in range(n - 1, -1, -1):
                count = 0 if (r, c) in mines_set else count + 1
                dp[r][c] = min(dp[r][c], count)
                
        for c in range(n):
            # Top
            count = 0
            for r in range(n):
                count = 0 if (r, c) in mines_set else count + 1
                dp[r][c] = min(dp[r][c], count)
                
            # Bottom
            count = 0
            for r in range(n - 1, -1, -1):
                count = 0 if (r, c) in mines_set else count + 1
                dp[r][c] = min(dp[r][c], count)
                
        return max(max(row) for row in dp)