# ──────────────────────────────────────────────────
# Problem  : 823. Binary Trees With Factors
# Difficulty: Medium
# Tags     : Array, Hash Table, Dynamic Programming, Sorting
# Link     : https://leetcode.com/problems/binary-trees-with-factors/
# Runtime  : 72 ms (beats 86%)
# Memory   : 12452000 (beats 88%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def numFactoredBinaryTrees(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7
        arr.sort()
        dp = {x: 1 for x in arr}

        for i, x in enumerate(arr):
            for j in range(i):
                left = arr[j]
                if left * left > x:
                    break
                if x % left == 0:
                    right = x // left
                    if right in dp:
                        if left == right:
                            dp[x] = (dp[x] + dp[left] * dp[right]) % MOD
                        else:
                            dp[x] = (dp[x] + dp[left] * dp[right] * 2) % MOD

        return sum(dp.values()) % MOD