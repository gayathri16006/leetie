# ──────────────────────────────────────────────────
# Problem  : 392. Is Subsequence
# Difficulty: Easy
# Tags     : Two Pointers, String, Dynamic Programming
# Link     : https://leetcode.com/problems/is-subsequence/
# Runtime  : 0 ms (beats 0%)
# Memory   : 12556000 (beats 0%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        i, j = 0, 0
        n, m = len(s), len(t)
        
        while i < n and j < m:
            if s[i] == t[j]:
                i += 1
            j += 1
            
        return i == n