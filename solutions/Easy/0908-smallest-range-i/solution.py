# ──────────────────────────────────────────────────
# Problem  : 908. Smallest Range I
# Difficulty: Easy
# Tags     : Array, Math
# Link     : https://leetcode.com/problems/smallest-range-i/
# Runtime  : 0 ms (beats 100%)
# Memory   : 13128000 (beats 70%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def smallestRangeI(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return max(0, max(nums) - min(nums) - 2 * k)