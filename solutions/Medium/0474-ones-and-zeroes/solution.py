# ──────────────────────────────────────────────────
# Problem  : 474. Ones and Zeroes
# Difficulty: Medium
# Tags     : Array, String, Dynamic Programming, Knapsack Problem, 0-1 Knapsack
# Link     : https://leetcode.com/problems/ones-and-zeroes/
# Runtime  : 0 ms (beats 0%)
# Memory   : 12368000 (beats 0%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        # dp[i][j] stores the maximum size of a subset using at most i zeros and j ones
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for s in strs:
            zeros = s.count('0')
            ones = s.count('1')

            # Traverse backwards to ensure each string is picked at most once (0/1 knapsack)
            for i in range(m, zeros - 1, -1):
                for j in range(n, ones - 1, -1):
                    dp[i][j] = max(dp[i][j], 1 + dp[i - zeros][j - ones])

        return dp[m][n]