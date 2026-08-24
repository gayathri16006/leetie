# ──────────────────────────────────────────────────
# Problem  : 594. Longest Harmonious Subsequence
# Difficulty: Easy
# Tags     : Array, Hash Table, Sliding Window, Sorting, Counting
# Link     : https://leetcode.com/problems/longest-harmonious-subsequence/
# Runtime  : 45 ms (beats 55%)
# Memory   : 14424000 (beats 26%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

from collections import Counter

class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counts = Counter(nums)
        max_len = 0
        
        for num in counts:
            if num + 1 in counts:
                max_len = max(max_len, counts[num] + counts[num + 1])
                
        return max_len