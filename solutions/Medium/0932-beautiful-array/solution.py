# ──────────────────────────────────────────────────
# Problem  : 932. Beautiful Array
# Difficulty: Medium
# Tags     : Array, Math, Divide and Conquer
# Link     : https://leetcode.com/problems/beautiful-array/
# Runtime  : 4 ms (beats 29%)
# Memory   : 12636000 (beats 15%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def beautifulArray(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = [1]
        
        while len(res) < n:
            # Generate odds: 2*x - 1, and evens: 2*x
            res = [2 * x - 1 for x in res] + [2 * x for x in res]
            
        # Filter down to numbers within the range [1, n]
        return [x for x in res if x <= n]