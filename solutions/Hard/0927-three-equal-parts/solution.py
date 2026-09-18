# ──────────────────────────────────────────────────
# Problem  : 927. Three Equal Parts
# Difficulty: Hard
# Tags     : Array, Math
# Link     : https://leetcode.com/problems/three-equal-parts/
# Runtime  : 35 ms (beats 7%)
# Memory   : 12964000 (beats 90%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def threeEqualParts(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        total_ones = sum(arr)
        
       
        if total_ones == 0:
            return [0, 2]
            
        # The number of 1s must be divisible by 3
        if total_ones % 3 != 0:
            return [-1, -1]
            
        k = total_ones // 3
        count = 0
        p1 = p2 = p3 = -1
        
        # Locate the starting 1 for each of the three parts
        for idx, val in enumerate(arr):
            if val == 1:
                count += 1
                if count == 1:
                    p1 = idx
                elif count == k + 1:
                    p2 = idx
                elif count == 2 * k + 1:
                    p3 = idx
                    
        
        n = len(arr)
        while p3 < n:
            if arr[p1] != arr[p2] or arr[p2] != arr[p3]:
                return [-1, -1]
            p1 += 1
            p2 += 1
            p3 += 1
            
        return [p1 - 1, p2]