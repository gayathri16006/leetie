# ──────────────────────────────────────────────────
# Problem  : 664. Strange Printer
# Difficulty: Hard
# Tags     : String, Dynamic Programming
# Link     : https://leetcode.com/problems/strange-printer/
# Runtime  : 143 ms (beats 83%)
# Memory   : 30560000 (beats 36%)
# Language : python3
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def strangePrinter(self, s: str) -> int:
        if not s:
            return 0
        
        # Deduplicate consecutive characters (e.g., "aaabbb" -> "ab")
        reduced = []
        for ch in s:
            if not reduced or reduced[-1] != ch:
                reduced.append(ch)
        s = "".join(reduced)
        n = len(s)
        
        memo = {}
        
        def dp(i: int, j: int) -> int:
            if i > j:
                return 0
            if i == j:
                return 1
            if (i, j) in memo:
                return memo[(i, j)]
            
            # Base transition: print s[i] separately
            res = dp(i, j - 1) + 1
            
            # Optimization: if s[k] matches s[j], print s[k...j] together
            for k in range(i, j):
                if s[k] == s[j]:
                    res = min(res, dp(i, k) + dp(k + 1, j - 1))
                    
            memo[(i, j)] = res
            return res
            
        return dp(0, n - 1)