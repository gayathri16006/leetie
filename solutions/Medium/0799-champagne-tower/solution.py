# ──────────────────────────────────────────────────
# Problem  : 799. Champagne Tower
# Difficulty: Medium
# Tags     : Dynamic Programming
# Link     : https://leetcode.com/problems/champagne-tower/
# Runtime  : 52 ms (beats 0%)
# Memory   : 19136000 (beats 0%)
# Language : python3
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        # dp[r][c] stores the total champagne that flows into glass (r, c)
        dp = [[0.0] * (r + 1) for r in range(query_row + 1)]
        dp[0][0] = poured
        
        for r in range(query_row):
            for c in range(r + 1):
                if dp[r][c] > 1:
                    # Excess champagne splits equally into (r + 1, c) and (r + 1, c + 1)
                    excess = (dp[r][c] - 1.0) / 2.0
                    dp[r + 1][c] += excess
                    dp[r + 1][c + 1] += excess
                    
        # A glass holds at most 1 cup of champagne
        return min(1.0, dp[query_row][query_glass])