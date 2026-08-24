# ──────────────────────────────────────────────────
# Problem  : 592. Fraction Addition and Subtraction
# Difficulty: Medium
# Tags     : Math, String, Simulation, Euclidean Algorithm, Greatest Common Divisor
# Link     : https://leetcode.com/problems/fraction-addition-and-subtraction/
# Runtime  : 0 ms (beats 0%)
# Memory   : 12640000 (beats 0%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

import re
from fractions import gcd  # For Python 2/3 compatibility (or math.gcd in Python 3)

class Solution(object):
    def fractionAddition(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        # Find all numerator and denominator pairs: [('num', 'den'), ...]
        fractions = re.findall(r'([+-]?\d+)/(\d+)', expression)
        
        curr_num = 0
        curr_den = 1
        
        def compute_gcd(a, b):
            while b:
                a, b = b, a % b
            return abs(a)
        
        for num, den in fractions:
            num = int(num)
            den = int(den)
            
            # a/b + c/d = (a*d + b*c) / (b*d)
            curr_num = curr_num * den + num * curr_den
            curr_den = curr_den * den
            
            # Reduce fraction at each step to prevent large intermediate numbers
            common = compute_gcd(curr_num, curr_den)
            curr_num //= common
            curr_den //= common
            
        return "{}/{}".format(curr_num, curr_den)