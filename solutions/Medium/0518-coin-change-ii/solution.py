# ──────────────────────────────────────────────────
# Problem  : 518. Coin Change II
# Difficulty: Medium
# Tags     : Array, Dynamic Programming, Knapsack Problem, Complete Knapsack
# Link     : https://leetcode.com/problems/coin-change-ii/
# Runtime  : 203 ms (beats 92%)
# Memory   : 19404000 (beats 84%)
# Language : python3
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def change(self, amount: int, coins: list[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1  # Base case: 1 way to make an amount of 0 (using no coins)

        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] += dp[x - coin]

        return dp[amount]