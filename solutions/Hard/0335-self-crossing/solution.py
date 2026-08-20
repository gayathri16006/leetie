# ──────────────────────────────────────────────────
# Problem  : 335. Self Crossing
# Difficulty: Hard
# Tags     : Array, Math, Geometry
# Link     : https://leetcode.com/problems/self-crossing/
# Runtime  : 39 ms (beats 77%)
# Memory   : 19760000 (beats 40%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def isSelfCrossing(self, distance):
        """
        :type distance: List[int]
        :rtype: bool
        """
        d = distance
        n = len(d)
        
        if n < 4:
            return False
        
        for i in range(3, n):
            # Case 1: Line i crosses line i - 3
            if d[i] >= d[i - 2] and d[i - 1] <= d[i - 3]:
                return True
            
            # Case 2: Line i overlaps line i - 4
            if i >= 4 and d[i - 1] == d[i - 3] and d[i] + d[i - 4] >= d[i - 2]:
                return True
            
            # Case 3: Line i crosses line i - 5
            if (i >= 5 and 
                d[i - 2] >= d[i - 4] and 
                d[i] + d[i - 4] >= d[i - 2] and 
                d[i - 1] <= d[i - 3] and 
                d[i - 1] + d[i - 5] >= d[i - 3]):
                return True
                
        return False