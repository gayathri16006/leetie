# ──────────────────────────────────────────────────
# Problem  : 115. Distinct Subsequences
# Difficulty: Hard
# Tags     : String, Dynamic Programming
# Link     : https://leetcode.com/problems/distinct-subsequences/
# Runtime  : 307 ms (beats 85%)
# Memory   : 12312000 (beats 89%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        m, n = len(s), len(t)
        
        dp = [0] * (n + 1)
        dp[0] = 1  
        
        for char_s in s:
            
            for j in range(n, 0, -1):
                if char_s == t[j - 1]:
                    dp[j] += dp[j - 1]
                    
        return dp[n]