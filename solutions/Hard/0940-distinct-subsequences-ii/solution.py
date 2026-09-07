# ──────────────────────────────────────────────────
# Problem  : 940. Distinct Subsequences II
# Difficulty: Hard
# Tags     : String, Dynamic Programming
# Link     : https://leetcode.com/problems/distinct-subsequences-ii/
# Runtime  : 13 ms (beats 23%)
# Memory   : 12296000 (beats 100%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def distinctSubseqII(self, s):
        """
        :type s: str
        :rtype: int
        """
        MOD = 10**9 + 7
        ends_with = [0] * 26

        for char in s:
            idx = ord(char) - ord('a')
            # 1 (for char itself) + sum of all distinct subsequences formed so far
            ends_with[idx] = (1 + sum(ends_with)) % MOD

        return sum(ends_with) % MOD