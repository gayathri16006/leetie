# ──────────────────────────────────────────────────
# Problem  : 730. Count Different Palindromic Subsequences
# Difficulty: Hard
# Tags     : String, Dynamic Programming
# Link     : https://leetcode.com/problems/count-different-palindromic-subsequences/
# Runtime  : 971 ms (beats 21%)
# Memory   : 42104000 (beats 65%)
# Language : python3
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def countPalindromicSubsequences(self, s: str) -> int:
        n = len(s)
        mod = 1_000_000_007
        
        # dp[i][j] stores the number of distinct palindromic subsequences in s[i...j]
        dp = [[0] * n for _ in range(n)]
        
        # Base case: single character strings
        for i in range(n):
            dp[i][i] = 1
            
        # Fill DP table for substring lengths from 2 to n
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                
                if s[i] == s[j]:
                    left = i + 1
                    right = j - 1
                    
                    # Find first and last occurrences of character s[i] inside s[i+1...j-1]
                    while left <= right and s[left] != s[i]:
                        left += 1
                    while left <= right and s[right] != s[i]:
                        right -= 1
                        
                    if left > right:
                        # No duplicates inside: s[i...j] is like 'a...a' with no 'a' inside
                        dp[i][j] = dp[i + 1][j - 1] * 2 + 2
                    elif left == right:
                        # Exactly one same character inside: like 'a...a...a'
                        dp[i][j] = dp[i + 1][j - 1] * 2 + 1
                    else:
                        # At least two same characters inside: subtract duplicate wraps
                        dp[i][j] = dp[i + 1][j - 1] * 2 - dp[left + 1][right - 1]
                else:
                    dp[i][j] = dp[i + 1][j] + dp[i][j - 1] - dp[i + 1][j - 1]
                    
                dp[i][j] = (dp[i][j] + mod) % mod
                
        return dp[0][n - 1]