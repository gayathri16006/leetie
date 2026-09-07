# ──────────────────────────────────────────────────
# Problem  : 935. Knight Dialer
# Difficulty: Medium
# Tags     : Dynamic Programming
# Link     : https://leetcode.com/problems/knight-dialer/
# Runtime  : 171 ms (beats 99%)
# Memory   : 12576000 (beats 65%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def knightDialer(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 10
        
        MOD = 10**9 + 7
        
        # dp[i] stores the number of ways to end at digit i
        dp = [1] * 10
        
        for _ in range(n - 1):
            next_dp = [0] * 10
            next_dp[0] = (dp[4] + dp[6]) % MOD
            next_dp[1] = (dp[6] + dp[8]) % MOD
            next_dp[2] = (dp[7] + dp[9]) % MOD
            next_dp[3] = (dp[4] + dp[8]) % MOD
            next_dp[4] = (dp[0] + dp[3] + dp[9]) % MOD
            next_dp[5] = 0
            next_dp[6] = (dp[0] + dp[1] + dp[7]) % MOD
            next_dp[7] = (dp[2] + dp[6]) % MOD
            next_dp[8] = (dp[1] + dp[3]) % MOD
            next_dp[9] = (dp[2] + dp[4]) % MOD
            
            dp = next_dp
            
        return sum(dp) % MOD