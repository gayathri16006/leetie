# ──────────────────────────────────────────────────
# Problem  : 628. Maximum Product of Three Numbers
# Difficulty: Easy
# Tags     : Array, Math, Sorting
# Link     : https://leetcode.com/problems/maximum-product-of-three-numbers/
# Runtime  : 0 ms (beats 0%)
# Memory   : 12448000 (beats 0%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        # Maximum can come from either:
        # 1. Product of the three largest numbers
        # 2. Product of the two smallest (negative) numbers and the largest number
        return max(nums[-1] * nums[-2] * nums[-3], nums[0] * nums[1] * nums[-1])