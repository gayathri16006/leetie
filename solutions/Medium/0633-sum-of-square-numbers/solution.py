# ──────────────────────────────────────────────────
# Problem  : 633. Sum of Square Numbers
# Difficulty: Medium
# Tags     : Math, Two Pointers, Binary Search
# Link     : https://leetcode.com/problems/sum-of-square-numbers/
# Runtime  : 0 ms (beats 0%)
# Memory   : 19232000 (beats 0%)
# Language : python3
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

import math

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left = 0
        right = math.isqrt(c)
        
        while left <= right:
            current_sum = left * left + right * right
            
            if current_sum == c:
                return True
            elif current_sum < c:
                left += 1
            else:
                right -= 1
                
        return False