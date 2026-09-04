# ──────────────────────────────────────────────────
# Problem  : 3903. Smallest Stable Index I
# Difficulty: Easy
# Tags     : Array, Prefix Sum
# Link     : https://leetcode.com/problems/smallest-stable-index-i/
# Runtime  : 5 ms (beats 88%)
# Memory   : 12428000 (beats 32%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def firstStableIndex(self, nums, k):
        n = len(nums)
        
        # suffix_min[i] stores min(nums[i..n-1])
        suffix_min = [0] * n
        suffix_min[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            suffix_min[i] = min(nums[i], suffix_min[i + 1])
            
        curr_max = float('-inf')
        for i in range(n):
            curr_max = max(curr_max, nums[i])
            if curr_max - suffix_min[i] <= k:
                return i
                
        return -1