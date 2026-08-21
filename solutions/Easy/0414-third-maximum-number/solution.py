# ──────────────────────────────────────────────────
# Problem  : 414. Third Maximum Number
# Difficulty: Easy
# Tags     : Array, Sorting
# Link     : https://leetcode.com/problems/third-maximum-number/
# Runtime  : 0 ms (beats 0%)
# Memory   : 12304000 (beats 0%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):

    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        first = second = third = None

        for num in nums:
            # Skip duplicates
            if num in (first, second, third):
                continue

            if first is None or num > first:
                third = second
                second = first
                first = num
            elif second is None or num > second:
                third = second
                second = num
            elif third is None or num > third:
                third = num

        # If the third maximum does not exist, return the maximum (first)
        return third if third is not None else first