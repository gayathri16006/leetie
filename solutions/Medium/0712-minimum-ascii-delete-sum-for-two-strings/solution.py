# ──────────────────────────────────────────────────
# Problem  : 712. Minimum ASCII Delete Sum for Two Strings
# Difficulty: Medium
# Tags     : String, Dynamic Programming, Longest Common Subsequence
# Link     : https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/
# Runtime  : 239 ms (beats 65%)
# Memory   : 19492000 (beats 85%)
# Language : python3
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        m, n = len(s1), len(s2)
        # dp[j] represents minimum delete sum for s1[...i] and s2[...j]
        dp = [0] * (n + 1)
        
        # Base case: s1 is empty, delete all chars in s2 prefix
        for j in range(1, n + 1):
            dp[j] = dp[j - 1] + ord(s2[j - 1])
            
        for i in range(1, m + 1):
            prev = dp[0]
            dp[0] += ord(s1[i - 1])
            
            for j in range(1, n + 1):
                temp = dp[j]
                if s1[i - 1] == s2[j - 1]:
                    dp[j] = prev
                else:
                    dp[j] = min(dp[j] + ord(s1[i - 1]), dp[j - 1] + ord(s2[j - 1]))
                prev = temp
                
        return dp[n]