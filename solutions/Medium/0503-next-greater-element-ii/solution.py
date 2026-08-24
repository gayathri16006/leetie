# ──────────────────────────────────────────────────
# Problem  : 503. Next Greater Element II
# Difficulty: Medium
# Tags     : Array, Stack, Monotonic Stack
# Link     : https://leetcode.com/problems/next-greater-element-ii/
# Runtime  : 16 ms (beats 91%)
# Memory   : 21224000 (beats 20%)
# Language : python3
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        n = len(nums)
        result = [-1] * n
        stack = []  # Stores indices of elements
        
        # Traverse the array twice to handle circularity
        for i in range(2 * n):
            current_idx = i % n
            # While stack is not empty and current element is greater than the element at stack top index
            while stack and nums[stack[-1]] < nums[current_idx]:
                prev_idx = stack.pop()
                result[prev_idx] = nums[current_idx]
            
            # Only push indices during the first pass
            if i < n:
                stack.append(current_idx)
                
        return result