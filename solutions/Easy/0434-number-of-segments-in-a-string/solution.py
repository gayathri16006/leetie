# ──────────────────────────────────────────────────
# Problem  : 434. Number of Segments in a String
# Difficulty: Easy
# Tags     : String
# Link     : https://leetcode.com/problems/number-of-segments-in-a-string/
# Runtime  : 0 ms (beats 0%)
# Memory   : 12220000 (beats 0%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.split())