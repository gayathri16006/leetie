# ──────────────────────────────────────────────────
# Problem  : 962. Maximum Width Ramp
# Difficulty: Medium
# Tags     : Array, Two Pointers, Stack, Monotonic Stack
# Link     : https://leetcode.com/problems/maximum-width-ramp/
# Runtime  : 0 ms (beats 0%)
# Memory   : 12420000 (beats 0%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def maxWidthRamp(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Step 1: Build a strictly decreasing monotonic stack of indices
        stack = []
        for i, val in enumerate(nums):
            if not stack or val < nums[stack[-1]]:
                stack.append(i)

        max_width = 0

        erse from right to left to find maximum ramp width
        for j in range(len(nums) - 1, -1, -1):
            while stack and nums[j] >= nums[stack[-1]]:
                max_width = max(max_width, j - stack.pop())

        return max_width