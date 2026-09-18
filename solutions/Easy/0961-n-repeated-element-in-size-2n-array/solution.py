# ──────────────────────────────────────────────────
# Problem  : 961. N-Repeated Element in Size 2N Array
# Difficulty: Easy
# Tags     : Array, Hash Table, Pigeonhole Principle
# Link     : https://leetcode.com/problems/n-repeated-element-in-size-2n-array/
# Runtime  : 0 ms (beats 0%)
# Memory   : 12272000 (beats 0%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def repeatedNTimes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen = set()
        for x in nums:
            if x in seen:
                return x
            seen.add(x)