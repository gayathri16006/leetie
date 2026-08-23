# ──────────────────────────────────────────────────
# Problem  : 553. Optimal Division
# Difficulty: Medium
# Tags     : Array, Math, Dynamic Programming
# Link     : https://leetcode.com/problems/optimal-division/
# Runtime  : 0 ms (beats 100%)
# Memory   : 12320000 (beats 51%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def optimalDivision(self, nums):
        if len(nums) == 1:
            return str(nums[0])
        if len(nums) == 2:
            return "{}/{}".format(nums[0], nums[1])
        
        # Wrap all elements from index 1 onward in parentheses
        return "{}/({})".format(nums[0], "/".join(map(str, nums[1:])))