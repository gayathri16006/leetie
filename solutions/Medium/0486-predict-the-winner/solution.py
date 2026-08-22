# ──────────────────────────────────────────────────
# Problem  : 486. Predict the Winner
# Difficulty: Medium
# Tags     : Array, Math, Dynamic Programming, Recursion, Minimax, Game Theory, Zero-Sum Game
# Link     : https://leetcode.com/problems/predict-the-winner/
# Runtime  : 3 ms (beats 60%)
# Memory   : 12376000 (beats 71%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def predictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        # If the number of elements is even, Player 1 can always force a win
        if n % 2 == 0:
            return True

        # dp[j] represents the maximum score difference for subarray ending at j
        dp = list(nums)

        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                dp[j] = max(nums[i] - dp[j], nums[j] - dp[j - 1])

        # Player 1 wins or ties if the net score difference is non-negative
        return dp[-1] >= 0