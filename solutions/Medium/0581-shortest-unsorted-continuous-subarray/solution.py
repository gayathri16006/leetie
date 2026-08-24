# ──────────────────────────────────────────────────
# Problem  : 581. Shortest Unsorted Continuous Subarray
# Difficulty: Medium
# Tags     : Array, Two Pointers, Stack, Greedy, Sorting, Monotonic Stack
# Link     : https://leetcode.com/problems/shortest-unsorted-continuous-subarray/
# Runtime  : 35 ms (beats 17%)
# Memory   : 13252000 (beats 61%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        start, end = -1, -2
        max_seen = nums[0]
        min_seen = nums[-1]
        
        # Traverse both directions simultaneously
        for i in range(1, n):
            # Left to right: find right boundary
            max_seen = max(max_seen, nums[i])
            if nums[i] < max_seen:
                end = i
            
            # Right to left: find left boundary
            min_seen = min(min_seen, nums[n - 1 - i])
            if nums[n - 1 - i] > min_seen:
                start = n - 1 - i
                
        return end - start + 1