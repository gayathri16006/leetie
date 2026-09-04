# ──────────────────────────────────────────────────
# Problem  : 910. Smallest Range II
# Difficulty: Medium
# Tags     : Array, Math, Greedy, Sorting
# Link     : https://leetcode.com/problems/smallest-range-ii/
# Runtime  : 35 ms (beats 75%)
# Memory   : 13360000 (beats 5%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def smallestRangeII(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        
        # Base difference without changing individual directions
        ans = nums[-1] - nums[0]

        for i in range(n - 1):
            high = max(nums[i] + k, nums[-1] - k)
            low = min(nums[0] + k, nums[i + 1] - k)
            ans = min(ans, high - low)

        return ans