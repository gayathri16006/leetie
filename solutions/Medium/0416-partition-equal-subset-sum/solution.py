# ──────────────────────────────────────────────────
# Problem  : 416. Partition Equal Subset Sum
# Difficulty: Medium
# Tags     : Array, Dynamic Programming, Knapsack Problem, 0-1 Knapsack
# Link     : https://leetcode.com/problems/partition-equal-subset-sum/
# Runtime  : 391 ms (beats 90%)
# Memory   : 12924000 (beats 53%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):

    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        total_sum = sum(nums)

        # An odd total cannot be split into two equal integer subsets
        if total_sum % 2 != 0:
            return False

        target = total_sum // 2
        dp = [False] * (target + 1)
        dp[0] = True  # Base case: sum of 0 is always achievable

        for num in nums:
            # Iterate backwards to ensure each number is used at most once
            for j in range(target, num - 1, -1):
                if dp[j - num]:
                    dp[j] = True

            # Early exit if target sum is found
            if dp[target]:
                return True

        return dp[target]