# ──────────────────────────────────────────────────
# Problem  : 494. Target Sum
# Difficulty: Medium
# Tags     : Array, Dynamic Programming, Backtracking, Knapsack Problem, 0-1 Knapsack
# Link     : https://leetcode.com/problems/target-sum/
# Runtime  : 27 ms (beats 86%)
# Memory   : 12436000 (beats 71%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        total_sum = sum(nums)
        
        # If the target is unreachable or the subset sum is not an integer
        if abs(target) > total_sum or (total_sum + target) % 2 != 0:
            return 0
        
        subset_target = (total_sum + target) // 2
        
        # dp[s] represents the number of ways to reach sum s
        dp = [0] * (subset_target + 1)
        dp[0] = 1  # 1 way to get sum 0 (empty subset)

        for num in nums:
            # Traverse backwards to ensure each number is used at most once
            for s in range(subset_target, num - 1, -1):
                dp[s] += dp[s - num]

        return dp[subset_target]