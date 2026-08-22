# ──────────────────────────────────────────────────
# Problem  : 456. 132 Pattern
# Difficulty: Medium
# Tags     : Array, Binary Search, Stack, Monotonic Stack, Ordered Set
# Link     : https://leetcode.com/problems/132-pattern/
# Runtime  : 0 ms (beats 0%)
# Memory   : 12472000 (beats 0%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 3:
            return False
        
        stack = []
        third = float('-inf')  # Represents candidate for nums[k]
        
        # Traverse backwards from right to left
        for num in reversed(nums):
            # If we find a number smaller than nums[k], a 132 pattern is found
            if num < third:
                return True
            
            # Maintain a monotonic decreasing stack; pop smaller elements into 'third'
            while stack and stack[-1] < num:
                third = stack.pop()
                
            stack.append(num)
            
        return False