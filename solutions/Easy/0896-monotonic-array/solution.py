# ──────────────────────────────────────────────────
# Problem  : 896. Monotonic Array
# Difficulty: Easy
# Tags     : Array
# Link     : https://leetcode.com/problems/monotonic-array/
# Runtime  : 47 ms (beats 80%)
# Memory   : 20380000 (beats 86%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def isMonotonic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        is_increasing = True
        is_decreasing = True

        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                is_increasing = False
            if nums[i] < nums[i + 1]:
                is_decreasing = False

            # Early exit if neither condition holds
            if not is_increasing and not is_decreasing:
                return False

        return True