# ──────────────────────────────────────────────────
# Problem  : 746. Min Cost Climbing Stairs
# Difficulty: Easy
# Tags     : Array, Dynamic Programming
# Link     : https://leetcode.com/problems/min-cost-climbing-stairs/
# Runtime  : 3 ms (beats 61%)
# Memory   : 19036000 (beats 100%)
# Language : python3
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        first = cost[0]
        second = cost[1]
        
        for i in range(2, len(cost)):
            current = cost[i] + min(first, second)
            first = second
            second = current
            
        return min(first, second)