# ──────────────────────────────────────────────────
# Problem  : 878. Nth Magical Number
# Difficulty: Hard
# Tags     : Math, Binary Search, Least Common Multiple, Inclusion-Exclusion Principle
# Link     : https://leetcode.com/problems/nth-magical-number/
# Runtime  : 0 ms (beats 100%)
# Memory   : 12392000 (beats 72%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

import math

class Solution(object):
    def nthMagicalNumber(self, n, a, b):
        """
        :type n: int
        :type a: int
        :type b: int
        :rtype: int
        """
        MOD = 10**9 + 7

        def gcd(x, y):
            while y:
                x, y = y, x % y
            return x

        lcm = (a * b) // gcd(a, b)

        left = min(a, b)
        right = n * min(a, b)

        while left < right:
            mid = (left + right) // 2
            
            # Count of magical numbers <= mid
            count = (mid // a) + (mid // b) - (mid // lcm)
            
            if count >= n:
                right = mid
            else:
                left = mid + 1

        return left % MOD