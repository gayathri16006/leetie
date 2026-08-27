# ──────────────────────────────────────────────────
# Problem  : 674. Longest Continuous Increasing Subsequence
# Difficulty: Easy
# Tags     : Array
# Link     : https://leetcode.com/problems/longest-continuous-increasing-subsequence/
# Runtime  : 0 ms (beats 0%)
# Memory   : 19396000 (beats 0%)
# Language : python3
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def findLengthOfLCIS(self, nums: list[int]) -> int:
        if not nums:
            return 0
        
        max_len = 1
        current_len = 1
        
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                current_len += 1
                max_len = max(max_len, current_len)
            else:
                current_len = 1
                
        return max_len