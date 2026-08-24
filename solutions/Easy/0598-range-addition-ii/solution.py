# ──────────────────────────────────────────────────
# Problem  : 598. Range Addition II
# Difficulty: Easy
# Tags     : Array, Math
# Link     : https://leetcode.com/problems/range-addition-ii/
# Runtime  : 0 ms (beats 0%)
# Memory   : 12312000 (beats 0%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        min_r = m
        min_c = n
        
        for r, c in ops:
            min_r = min(min_r, r)
            min_c = min(min_c, c)
            
        return min_r * min_c