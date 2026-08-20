# ──────────────────────────────────────────────────
# Problem  : 365. Water and Jug Problem
# Difficulty: Medium
# Tags     : Math, Depth-First Search, Breadth-First Search, Bézout's Lemma, Euclidean Algorithm, Greatest Common Divisor, Extended Euclidean Algorithm
# Link     : https://leetcode.com/problems/water-and-jug-problem/
# Runtime  : 0 ms (beats 100%)
# Memory   : 12328000 (beats 61%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def canMeasureWater(self, x, y, target):
        """
        :type x: int
        :type y: int
        :type target: int
        :rtype: bool
        """
        if target > x + y:
            return False
        
        if target == 0:
            return True
        
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        return target % gcd(x, y) == 0