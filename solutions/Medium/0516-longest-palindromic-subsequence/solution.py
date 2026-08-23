# ──────────────────────────────────────────────────
# Problem  : 516. Longest Palindromic Subsequence
# Difficulty: Medium
# Tags     : String, Dynamic Programming
# Link     : https://leetcode.com/problems/longest-palindromic-subsequence/
# Runtime  : 0 ms (beats 0%)
# Memory   : 12516000 (beats 0%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def longestPalindromeSubseq(self, s):
        n = len(s)
        # dp[i][j] stores the length of the LPS in substring s[i:j+1]
        dp = [[0] * n for _ in range(n)]
        
        # Every single character is a palindrome of length 1
        for i in range(n):
            dp[i][i] = 1
            
        # Iterate over substring lengths from 2 to n
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    dp[i][j] = 2 + (dp[i + 1][j - 1] if length > 2 else 0)
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
                    
        return dp[0][n - 1]