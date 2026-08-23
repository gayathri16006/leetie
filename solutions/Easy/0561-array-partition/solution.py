# ──────────────────────────────────────────────────
# Problem  : 561. Array Partition
# Difficulty: Easy
# Tags     : Array, Greedy, Sorting, Counting Sort
# Link     : https://leetcode.com/problems/array-partition/
# Runtime  : 31 ms (beats 91%)
# Memory   : 14032000 (beats 9%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def arrayPairSum(self, nums):
        nums.sort()
        return sum(nums[::2])