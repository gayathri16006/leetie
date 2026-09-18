# ──────────────────────────────────────────────────
# Problem  : 956. Tallest Billboard
# Difficulty: Hard
# Tags     : Array, Dynamic Programming, Meet in the Middle, Knapsack Problem, 0-1 Knapsack
# Link     : https://leetcode.com/problems/tallest-billboard/
# Runtime  : 335 ms (beats 88%)
# Memory   : 13624000 (beats 25%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def tallestBillboard(self, rods):
        """
        :type rods: List[int]
        :rtype: int
        """
        # dp[diff] = max height of the shorter support when difference is diff
        dp = {0: 0}
        
        for rod in rods:
            new_dp = dict(dp)
            for diff, shorter in dp.items():
                taller = shorter + diff
                
                # Option 1: Put rod on the taller side
                # New difference is diff + rod; shorter side remains unchanged
                new_diff = diff + rod
                new_dp[new_diff] = max(new_dp.get(new_diff, 0), shorter)
                
                # Option 2: Put rod on the shorter side
                if rod <= diff:
                    # Shorter side increases, but is still shorter or equal
                    new_diff = diff - rod
                    new_dp[new_diff] = max(new_dp.get(new_diff, 0), shorter + rod)
                else:
                    
                    new_diff = rod - diff
                    new_dp[new_diff] = max(new_dp.get(new_diff, 0), taller)
                    
            dp = new_dp
            
        return dp.get(0, 0)