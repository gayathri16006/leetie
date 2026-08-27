# ──────────────────────────────────────────────────
# Problem  : 740. Delete and Earn
# Difficulty: Medium
# Tags     : Array, Hash Table, Dynamic Programming
# Link     : https://leetcode.com/problems/delete-and-earn/
# Runtime  : 11 ms (beats 32%)
# Memory   : 20928000 (beats 57%)
# Language : python3
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

from collections import Counter

class Solution:
    def deleteAndEarn(self, nums: list[int]) -> int:
        if not nums:
            return 0
        
        # Calculate total points gained from taking each distinct value
        points = Counter()
        max_num = 0
        for num in nums:
            points[num] += num
            if num > max_num:
                max_num = num

        # House Robber DP pattern
        prev2 = 0  # dp[i-2]
        prev1 = points[1]  # dp[i-1]

        for i in range(2, max_num + 1):
            curr = max(prev1, prev2 + points[i])
            prev2 = prev1
            prev1 = curr

        return prev1