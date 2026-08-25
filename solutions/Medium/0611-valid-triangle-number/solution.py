# ──────────────────────────────────────────────────
# Problem  : 611. Valid Triangle Number
# Difficulty: Medium
# Tags     : Array, Two Pointers, Binary Search, Greedy, Sorting
# Link     : https://leetcode.com/problems/valid-triangle-number/
# Runtime  : 459 ms (beats 46%)
# Memory   : 19264000 (beats 78%)
# Language : python3
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

from typing import List

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        count = 0
        n = len(nums)
        
        # Fix the longest side at index k from right to left
        for k in range(n - 1, 1, -1):
            i = 0
            j = k - 1
            
            while i < j:
                # If nums[i] + nums[j] > nums[k], then every index from i to j-1 
                # paired with j will also satisfy the condition (nums[x] + nums[j] > nums[k])
                if nums[i] + nums[j] > nums[k]:
                    count += (j - i)
                    j -= 1
                else:
                    i += 1
                    
        return count