# ──────────────────────────────────────────────────
# Problem  : 638. Shopping Offers
# Difficulty: Medium
# Tags     : Array, Dynamic Programming, Backtracking, Bit Manipulation, Memoization, Bitmask, Knapsack Problem, Complete Knapsack
# Link     : https://leetcode.com/problems/shopping-offers/
# Runtime  : 27 ms (beats 28%)
# Memory   : 19560000 (beats 77%)
# Language : python3
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def shoppingOffers(self, price: list[int], special: list[list[int]], needs: list[int]) -> int:
        memo = {}

        def dfs(cur_needs: tuple[int, ...]) -> int:
            if cur_needs in memo:
                return memo[cur_needs]

            # 1. Base case: buy all remaining needs at regular price
            min_cost = sum(need * p for need, p in zip(cur_needs, price))

            # 2. Try applying each special offer
            for offer in special:
                offer_items = offer[:-1]
                offer_price = offer[-1]

                # Check if this special offer exceeds any item requirement
                if all(c >= o for c, o in zip(cur_needs, offer_items)):
                    updated_needs = tuple(c - o for c, o in zip(cur_needs, offer_items))
                    min_cost = min(min_cost, offer_price + dfs(updated_needs))

            memo[cur_needs] = min_cost
            return min_cost

        return dfs(tuple(needs))