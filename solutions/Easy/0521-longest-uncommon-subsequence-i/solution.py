# ──────────────────────────────────────────────────
# Problem  : 521. Longest Uncommon Subsequence I
# Difficulty: Easy
# Tags     : String
# Link     : https://leetcode.com/problems/longest-uncommon-subsequence-i/
# Runtime  : 0 ms (beats 100%)
# Memory   : 12412000 (beats 17%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def findLUSlength(self, a, b):
        if a == b:
            return -1
        return max(len(a), len(b))