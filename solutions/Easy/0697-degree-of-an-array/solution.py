# ──────────────────────────────────────────────────
# Problem  : 697. Degree of an Array
# Difficulty: Easy
# Tags     : Array, Hash Table
# Link     : https://leetcode.com/problems/degree-of-an-array/
# Runtime  : 0 ms (beats 0%)
# Memory   : 19336000 (beats 0%)
# Language : python3
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

from collections import defaultdict
from typing import List

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        first_occurrence = {}
        last_occurrence = {}
        count = defaultdict(int)
        
        # Track frequency and boundary indices for each number
        for i, num in enumerate(nums):
            if num not in first_occurrence:
                first_occurrence[num] = i
            last_occurrence[num] = i
            count[num] += 1
            
        degree = max(count.values())
        min_length = len(nums)
        
        # Find the minimum subarray length among all elements with the maximum frequency
        for num, freq in count.items():
            if freq == degree:
                min_length = min(min_length, last_occurrence[num] - first_occurrence[num] + 1)
                
        return min_length