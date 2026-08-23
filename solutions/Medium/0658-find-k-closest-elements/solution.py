# ──────────────────────────────────────────────────
# Problem  : 658. Find K Closest Elements
# Difficulty: Medium
# Tags     : Array, Two Pointers, Binary Search, Sliding Window, Sorting, Heap (Priority Queue)
# Link     : https://leetcode.com/problems/find-k-closest-elements/
# Runtime  : 0 ms (beats 0%)
# Memory   : 12172000 (beats 0%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        left = 0
        right = len(arr) - k

        while left < right:
            mid = (left + right) // 2
            # Compare distances of endpoints: arr[mid] vs arr[mid + k]
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid

        return arr[left:left + k]