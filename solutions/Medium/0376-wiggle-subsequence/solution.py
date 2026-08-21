# ──────────────────────────────────────────────────
# Problem  : 376. Wiggle Subsequence
# Difficulty: Medium
# Tags     : Array, Dynamic Programming, Greedy
# Link     : https://leetcode.com/problems/wiggle-subsequence/
# Runtime  : 0 ms (beats 100%)
# Memory   : 12332000 (beats 69%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        up = 1
        down = 1
        
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                up = down + 1
            elif nums[i] < nums[i - 1]:
                down = up + 1
                
        return max(up, down)