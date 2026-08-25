# ──────────────────────────────────────────────────
# Problem  : 639. Decode Ways II
# Difficulty: Hard
# Tags     : String, Dynamic Programming
# Link     : https://leetcode.com/problems/decode-ways-ii/
# Runtime  : 255 ms (beats 56%)
# Memory   : 20020000 (beats 63%)
# Language : python3
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def numDecodings(self, s: str) -> int:
        MOD = 10**9 + 7
        
        # Base counts for DP space optimization
        first = 1  # dp[i-2]
        
        # Determine decode ways for first character (dp[i-1])
        if s[0] == '*':
            second = 9
        elif s[0] == '0':
            second = 0
        else:
            second = 1
            
        def ways1(c: str) -> int:
            if c == '*':
                return 9
            if c == '0':
                return 0
            return 1

        def ways2(c1: str, c2: str) -> int:
            if c1 == '*' and c2 == '*':
                # 11-19 (9) + 21-26 (6) = 15
                return 15
            if c1 == '*':
                # If c2 <= '6', '*' can be '1' or '2'; else '*' can only be '1'
                return 2 if c2 <= '6' else 1
            if c2 == '*':
                if c1 == '1':
                    return 9  # 11-19
                if c1 == '2':
                    return 6  # 21-26
                return 0
            # Both are digits
            val = int(c1 + c2)
            return 1 if 10 <= val <= 26 else 0

        for i in range(1, len(s)):
            current = (second * ways1(s[i]) + first * ways2(s[i - 1], s[i])) % MOD
            first = second
            second = current
            
        return second