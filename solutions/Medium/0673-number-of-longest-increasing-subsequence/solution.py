# ──────────────────────────────────────────────────
# Problem  : 673. Number of Longest Increasing Subsequence
# Difficulty: Medium
# Tags     : Array, Dynamic Programming, Binary Indexed Tree, Segment Tree, Longest Increasing Subsequence
# Link     : https://leetcode.com/problems/number-of-longest-increasing-subsequence/
# Runtime  : 469 ms (beats 75%)
# Memory   : 19456000 (beats 65%)
# Language : python3
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

from typing import List

class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        n = len(nums)
        # lengths[i]: length of the longest increasing subsequence ending at index i
        lengths = [1] * n
        # counts[i]: number of longest increasing subsequences ending at index i
        counts = [1] * n
        
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    if lengths[j] + 1 > lengths[i]:
                        lengths[i] = lengths[j] + 1
                        counts[i] = counts[j]
                    elif lengths[j] + 1 == lengths[i]:
                        counts[i] += counts[j]
                        
        max_len = max(lengths)
        
        # Sum up counts for all subsequences achieving the maximum length
        return sum(c for l, c in zip(lengths, counts) if l == max_len)