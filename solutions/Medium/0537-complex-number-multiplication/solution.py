# ──────────────────────────────────────────────────
# Problem  : 537. Complex Number Multiplication
# Difficulty: Medium
# Tags     : Math, String, Simulation
# Link     : https://leetcode.com/problems/complex-number-multiplication/
# Runtime  : 0 ms (beats 0%)
# Memory   : 12472000 (beats 0%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def complexNumberMultiply(self, num1, num2):
        # Parse real and imaginary parts
        r1, i1 = num1[:-1].split('+')
        r2, i2 = num2[:-1].split('+')
        
        a, b = int(r1), int(i1)
        c, d = int(r2), int(i2)
        
        # Compute real and imaginary results
        real_part = a * c - b * d
        imag_part = a * d + b * c
        
        return "{}+{}i".format(real_part, imag_part)