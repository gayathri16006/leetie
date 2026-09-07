# ──────────────────────────────────────────────────
# Problem  : 918. Maximum Sum Circular Subarray
# Difficulty: Medium
# Tags     : Array, Divide and Conquer, Dynamic Programming, Queue, Monotonic Queue
# Link     : https://leetcode.com/problems/maximum-sum-circular-subarray/
# Runtime  : 83 ms (beats 91%)
# Memory   : 14976000 (beats 62%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def maxSubarraySumCircular(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total_sum = 0
        cur_max = 0
        max_sum = nums[0]
        cur_min = 0
        min_sum = nums[0]

        for x in nums:
            # Standard Kadane's for max subarray sum
            cur_max = max(x, cur_max + x)
            max_sum = max(max_sum, cur_max)

            # Kadane's for min subarray sum
            cur_min = min(x, cur_min + x)
            min_sum = min(min_sum, cur_min)

            total_sum += x

        # If all numbers are negative, max_sum is the largest single element
        if max_sum < 0:
            return max_sum

        return max(max_sum, total_sum - min_sum)