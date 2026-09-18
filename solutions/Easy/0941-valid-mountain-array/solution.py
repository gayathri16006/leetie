# ──────────────────────────────────────────────────
# Problem  : 941. Valid Mountain Array
# Difficulty: Easy
# Tags     : Array
# Link     : https://leetcode.com/problems/valid-mountain-array/
# Runtime  : 125 ms (beats 100%)
# Memory   : 13776000 (beats 28%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        n = len(arr)
        if n < 3:
            return False
        
        i = 0
        
        # Walk up
        while i + 1 < n and arr[i] < arr[i + 1]:
            i += 1
            
        # Peak cannot be the first or last element
        if i == 0 or i == n - 1:
            return False
            
        # Walk down
        while i + 1 < n and arr[i] > arr[i + 1]:
            i += 1
            
        return i == n - 1