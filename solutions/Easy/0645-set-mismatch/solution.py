# ──────────────────────────────────────────────────
# Problem  : 645. Set Mismatch
# Difficulty: Easy
# Tags     : Array, Hash Table, Bit Manipulation, Sorting
# Link     : https://leetcode.com/problems/set-mismatch/
# Runtime  : 4 ms (beats 93%)
# Memory   : 21128000 (beats 15%)
# Language : python3
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

from typing import List

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # Expected sum for numbers from 1 to n: n * (n + 1) // 2
        expected_sum = n * (n + 1) // 2
        actual_sum = sum(nums)
        unique_sum = sum(set(nums))
        
        # Duplicate = actual_sum - unique_sum
        duplicate = actual_sum - unique_sum
        
        # Missing = expected_sum - unique_sum
        missing = expected_sum - unique_sum
        
        return [duplicate, missing]