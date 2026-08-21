# ──────────────────────────────────────────────────
# Problem  : 403. Frog Jump
# Difficulty: Hard
# Tags     : Array, Dynamic Programming
# Link     : https://leetcode.com/problems/frog-jump/
# Runtime  : 135 ms (beats 51%)
# Memory   : 13884000 (beats 96%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):

    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        # Map each stone to the set of jump sizes that can land on it
        dp = {stone: set() for stone in stones}
        dp[0].add(0)

        target = stones[-1]

        for stone in stones:
            for k in dp[stone]:
                # Next possible jumps from this stone
                for step in (k - 1, k, k + 1):
                    if step > 0 and (stone + step) in dp:
                        dp[stone + step].add(step)

        return len(dp[target]) > 0