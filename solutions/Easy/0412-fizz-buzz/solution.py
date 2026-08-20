# ──────────────────────────────────────────────────
# Problem  : 412. Fizz Buzz
# Difficulty: Easy
# Tags     : Math, String, Simulation
# Link     : https://leetcode.com/problems/fizz-buzz/
# Runtime  : 4 ms (beats 18%)
# Memory   : 13312000 (beats 42%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []
        for i in range(1, n + 1):
            if i % 15 == 0:
                ans.append("FizzBuzz")
            elif i % 3 == 0:
                ans.append("Fizz")
            elif i % 5 == 0:
                ans.append("Buzz")
            else:
                ans.append(str(i))
        return ans