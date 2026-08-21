# ──────────────────────────────────────────────────
# Problem  : 322. Coin Change
# Difficulty: Medium
# Tags     : Array, Dynamic Programming, Breadth-First Search, Knapsack Problem, Complete Knapsack
# Link     : https://leetcode.com/problems/coin-change/
# Runtime  : 908 ms (beats 40%)
# Memory   : 12980000 (beats 63%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):

    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # Initialize dp array with an unreachable upper bound (amount + 1)
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0  # Base case: 0 coins needed to make amount 0

        for i in range(1, amount + 1):
            for c in coins:
                if i - c >= 0:
                    dp[i] = min(dp[i], 1 + dp[i - c])

        return dp[amount] if dp[amount] != float("inf") else -1