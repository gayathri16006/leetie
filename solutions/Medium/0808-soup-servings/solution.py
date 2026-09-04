# ──────────────────────────────────────────────────
# Problem  : 808. Soup Servings
# Difficulty: Medium
# Tags     : Math, Dynamic Programming, Probability and Statistics
# Link     : https://leetcode.com/problems/soup-servings/
# Runtime  : 15 ms (beats 83%)
# Memory   : 14368000 (beats 19%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def soupServings(self, n):
        """
        :type n: int
        :rtype: float
        """
        # Threshold: for large n, P(A empties first) -> 1.0 within 1e-5
        if n >= 4800:
            return 1.0

        # Scale down by 25 mL
        m = (n + 24) // 25
        memo = {}

        def dp(a, b):
            if a <= 0 and b <= 0:
                return 0.5
            if a <= 0:
                return 1.0
            if b <= 0:
                return 0.0
            if (a, b) in memo:
                return memo[(a, b)]

            res = 0.25 * (
                dp(a - 4, b) +
                dp(a - 3, b - 1) +
                dp(a - 2, b - 2) +
                dp(a - 1, b - 3)
            )
            memo[(a, b)] = res
            return res

        return dp(m, m)