# ──────────────────────────────────────────────────
# Problem  : 413. Arithmetic Slices
# Difficulty: Medium
# Tags     : Array, Dynamic Programming, Sliding Window
# Link     : https://leetcode.com/problems/arithmetic-slices/
# Runtime  : 0 ms (beats 100%)
# Memory   : 12488000 (beats 97%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def numberOfArithmeticSlices(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n < 3:
            return 0
        
        total_slices = 0
        current_slices = 0
        
        for i in range(2, n):
            # Check if current three elements form an arithmetic progression
            if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
                current_slices += 1
                total_slices += current_slices
            else:
                current_slices = 0
                
        return total_slices