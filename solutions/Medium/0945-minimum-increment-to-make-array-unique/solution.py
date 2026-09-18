# ──────────────────────────────────────────────────
# Problem  : 945. Minimum Increment to Make Array Unique
# Difficulty: Medium
# Tags     : Array, Greedy, Sorting, Counting
# Link     : https://leetcode.com/problems/minimum-increment-to-make-array-unique/
# Runtime  : 190 ms (beats 64%)
# Memory   : 20664000 (beats 35%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def minIncrementForUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        moves = 0
        
        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                needed = nums[i - 1] + 1
                moves += needed - nums[i]
                nums[i] = needed
                
        return moves