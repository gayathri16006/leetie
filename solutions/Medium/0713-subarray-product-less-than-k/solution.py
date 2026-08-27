# ──────────────────────────────────────────────────
# Problem  : 713. Subarray Product Less Than K
# Difficulty: Medium
# Tags     : Array, Binary Search, Sliding Window, Prefix Sum
# Link     : https://leetcode.com/problems/subarray-product-less-than-k/
# Runtime  : 12 ms (beats 100%)
# Memory   : 21628000 (beats 10%)
# Language : python3
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        if k <= 1:
            return 0

        product = 1
        left = 0
        ans = 0

        for right, val in enumerate(nums):
            product *= val
            while product >= k:
                product //= nums[left]
                left += 1
            # Number of contiguous subarrays ending at 'right' is right - left + 1
            ans += right - left + 1

        return ans