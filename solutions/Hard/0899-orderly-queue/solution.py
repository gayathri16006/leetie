# ──────────────────────────────────────────────────
# Problem  : 899. Orderly Queue
# Difficulty: Hard
# Tags     : Math, String, Sorting, Lexicographically Minimal String Rotation
# Link     : https://leetcode.com/problems/orderly-queue/
# Runtime  : 0 ms (beats 0%)
# Memory   : 12364000 (beats 0%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def orderlyQueue(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        if k == 1:
            # Only cyclic rotations are possible
            return min(s[i:] + s[:i] for i in range(len(s)))
        else:
            # Any permutation is possible
            return "".join(sorted(s))