# ──────────────────────────────────────────────────
# Problem  : 583. Delete Operation for Two Strings
# Difficulty: Medium
# Tags     : String, Dynamic Programming, Longest Common Subsequence
# Link     : https://leetcode.com/problems/delete-operation-for-two-strings/
# Runtime  : 136 ms (beats 94%)
# Memory   : 14456000 (beats 77%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def minDistance(self, word1, word2):
        m, n = len(word1), len(word2)
        
        # dp[i][j] stores the LCS length of word1[:i] and word2[:j]
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                    
        lcs_length = dp[m][n]
        return (m - lcs_length) + (n - lcs_length)