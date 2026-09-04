# ──────────────────────────────────────────────────
# Problem  : 829. Consecutive Numbers Sum
# Difficulty: Hard
# Tags     : Math, Enumeration
# Link     : https://leetcode.com/problems/consecutive-numbers-sum/
# Runtime  : 91 ms (beats 70%)
# Memory   : 12400000 (beats 64%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def consecutiveNumbersSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        k = 1
        
        while True:
            # Triangular sum for k - 1 items
            triangular = k * (k - 1) // 2
            remainder = n - triangular
            
            if remainder <= 0:
                break
                
            if remainder % k == 0:
                count += 1
                
            k += 1
            
        return count