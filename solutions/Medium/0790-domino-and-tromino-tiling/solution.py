# ──────────────────────────────────────────────────
# Problem  : 790. Domino and Tromino Tiling
# Difficulty: Medium
# Tags     : Dynamic Programming
# Link     : https://leetcode.com/problems/domino-and-tromino-tiling/
# Runtime  : 2 ms (beats 59%)
# Memory   : 19240000 (beats 78%)
# Language : python3
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def numTilings(self, n: int) -> int:
        if n <= 2:
            return n
        if n == 3:
            return 5
            
        MOD = 1_000_000_007
        
        # Base states for n = 1, 2, 3
        # Recurrence: dp[i] = (2 * dp[i - 1] + dp[i - 3]) % MOD
        dp_3 = 1  # dp[1]
        dp_2 = 2  # dp[2]
        dp_1 = 5  # dp[3]
        
        for _ in range(4, n + 1):
            curr = (2 * dp_1 + dp_3) % MOD
            dp_3 = dp_2
            dp_2 = dp_1
            dp_1 = curr
            
        return dp_1