# ──────────────────────────────────────────────────
# Problem  : 334. Increasing Triplet Subsequence
# Difficulty: Medium
# Tags     : Array, Greedy, Longest Increasing Subsequence
# Link     : https://leetcode.com/problems/increasing-triplet-subsequence/
# Runtime  : 0 ms (beats 0%)
# Memory   : 12484000 (beats 0%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        first = float('inf')
        second = float('inf')
        
        for num in nums:
            if num <= first:
                first = num          # Update smallest so far
            elif num <= second:
                second = num         # Update second smallest
            else:
                # Found a number larger than both first and second
                return True
                
        return False