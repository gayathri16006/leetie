# ──────────────────────────────────────────────────
# Problem  : 521. Longest Uncommon Subsequence I
# Difficulty: Easy
# Tags     : String
# Link     : https://leetcode.com/problems/longest-uncommon-subsequence-i/
# Runtime  : 0 ms (beats 0%)
# Memory   : 12236000 (beats 0%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def findLUSlength(self, a, b):
        if a == b:
            return -1
        return max(len(a), len(b))