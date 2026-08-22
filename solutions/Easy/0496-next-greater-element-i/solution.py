# ──────────────────────────────────────────────────
# Problem  : 496. Next Greater Element I
# Difficulty: Easy
# Tags     : Array, Hash Table, Stack, Monotonic Stack
# Link     : https://leetcode.com/problems/next-greater-element-i/
# Runtime  : 6 ms (beats 31%)
# Memory   : 12688000 (beats 24%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        next_greater = {}
        stack = []

        for num in nums2:
            # If the current number is greater than elements on the stack,
            # it is their next greater element.
            while stack and stack[-1] < num:
                next_greater[stack.pop()] = num
            stack.append(num)

        # Build the result for nums1 using the map (default to -1)
        return [next_greater.get(x, -1) for x in nums1]