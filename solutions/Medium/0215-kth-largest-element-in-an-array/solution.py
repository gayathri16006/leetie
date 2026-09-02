# ──────────────────────────────────────────────────
# Problem  : 215. Kth Largest Element in an Array
# Difficulty: Medium
# Tags     : Array, Divide and Conquer, Sorting, Heap (Priority Queue), Quickselect
# Link     : https://leetcode.com/problems/kth-largest-element-in-an-array/
# Runtime  : 77 ms (beats 89%)
# Memory   : 20008000 (beats 92%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def findKthLargest(self, nums, k):
        nums.sort(reverse=True)
        return nums[k - 1]