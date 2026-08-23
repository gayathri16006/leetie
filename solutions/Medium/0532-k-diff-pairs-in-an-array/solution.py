# ──────────────────────────────────────────────────
# Problem  : 532. K-diff Pairs in an Array
# Difficulty: Medium
# Tags     : Array, Hash Table, Two Pointers, Binary Search, Sorting
# Link     : https://leetcode.com/problems/k-diff-pairs-in-an-array/
# Runtime  : 7 ms (beats 70%)
# Memory   : 14112000 (beats 55%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

from collections import Counter

class Solution(object):
    def findPairs(self, nums, k):
        if k < 0:
            return 0
        
        count = Counter(nums)
        pairs = 0
        
        for num in count:
            if k == 0:
                if count[num] >= 2:
                    pairs += 1
            else:
                if num + k in count:
                    pairs += 1
                    
        return pairs