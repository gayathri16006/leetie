# ──────────────────────────────────────────────────
# Problem  : 470. Implement Rand10() Using Rand7()
# Difficulty: Medium
# Tags     : Math, Rejection Sampling, Randomized, Probability and Statistics
# Link     : https://leetcode.com/problems/implement-rand10-using-rand7/
# Runtime  : 324 ms (beats 57%)
# Memory   : 17544000 (beats 22%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

# The rand7() API is already defined for you.
# @return a random integer in the range 1 to 7

class Solution(object):
    def rand10(self):
        """
        :rtype: int
        """
        while True:
            row = rand7()
            col = rand7()
            num = (row - 1) * 7 + col  # Uniform integer in [1, 49]
            
            if num <= 40:
                return 1 + (num - 1) % 10