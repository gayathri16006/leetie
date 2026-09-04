# ──────────────────────────────────────────────────
# Problem  : 852. Peak Index in a Mountain Array
# Difficulty: Medium
# Tags     : Array, Binary Search, Ternary Search
# Link     : https://leetcode.com/problems/peak-index-in-a-mountain-array/
# Runtime  : 0 ms (beats 100%)
# Memory   : 21700000 (beats 39%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        left, right = 0, len(arr) - 1

        while left < right:
            mid = (left + right) // 2
            if arr[mid] < arr[mid + 1]:
                left = mid + 1
            else:
                right = mid

        return left