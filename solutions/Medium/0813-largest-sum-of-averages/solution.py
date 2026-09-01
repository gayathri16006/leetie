# ──────────────────────────────────────────────────
# Problem  : 813. Largest Sum of Averages
# Difficulty: Medium
# Tags     : Array, Dynamic Programming, Prefix Sum
# Link     : https://leetcode.com/problems/largest-sum-of-averages/
# Runtime  : 157 ms (beats 70%)
# Memory   : 12468000 (beats 72%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def largestSumOfAverages(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        # dp[i] represents the maximum score partitioning nums[:i] into at most `p` parts
        dp = [prefix[i] / float(i) if i > 0 else 0.0 for i in range(n + 1)]

        # Iterate through number of partitions from 2 to k
        for p in range(2, k + 1):
            for i in range(n, p - 1, -1):
                for j in range(p - 1, i):
                    avg = (prefix[i] - prefix[j]) / float(i - j)
                    dp[i] = max(dp[i], dp[j] + avg)

        return dp[n]