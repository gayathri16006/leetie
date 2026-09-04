# ──────────────────────────────────────────────────
# Problem  : 905. Sort Array By Parity
# Difficulty: Easy
# Tags     : Array, Two Pointers, Sorting
# Link     : https://leetcode.com/problems/sort-array-by-parity/
# Runtime  : 4 ms (beats 37%)
# Memory   : 13008000 (beats 35%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left, right = 0, len(nums) - 1

        while left < right:
            if nums[left] % 2 > nums[right] % 2:
                nums[left], nums[right] = nums[right], nums[left]

            if nums[left] % 2 == 0:
                left += 1
            if nums[right] % 2 == 1:
                right -= 1

        return nums