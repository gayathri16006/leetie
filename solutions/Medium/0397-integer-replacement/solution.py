# ──────────────────────────────────────────────────
# Problem  : 397. Integer Replacement
# Difficulty: Medium
# Tags     : Dynamic Programming, Greedy, Bit Manipulation, Memoization
# Link     : https://leetcode.com/problems/integer-replacement/
# Runtime  : 0 ms (beats 100%)
# Memory   : 12344000 (beats 53%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        operations = 0
        
        while n > 1:
            if n % 2 == 0:
                n //= 2
            elif n == 3:
                # Special case: 3 -> 2 -> 1 takes fewer steps than 3 -> 4 -> 2 -> 1
                n -= 1
            elif n % 4 == 3:
                # Ending in binary '11': adding 1 creates more trailing zeros
                n += 1
            else:
                # Ending in binary '01': subtracting 1 removes the lowest bit
                n -= 1
                
            operations += 1
            
        return operations