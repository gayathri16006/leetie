# ──────────────────────────────────────────────────
# Problem  : 546. Remove Boxes
# Difficulty: Hard
# Tags     : Array, Dynamic Programming, Memoization
# Link     : https://leetcode.com/problems/remove-boxes/
# Runtime  : 1371 ms (beats 33%)
# Memory   : 24936000 (beats 26%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def removeBoxes(self, boxes):
        """
        :type boxes: List[int]
        :rtype: int
        """
        memo = {}

        def dp(l, r, k):
            if l > r:
                return 0
            
            # Optimization: merge consecutive identical elements at the start
            while l + 1 <= r and boxes[l] == boxes[l + 1]:
                l += 1
                k += 1
                
            state = (l, r, k)
            if state in memo:
                return memo[state]
            
            # Option 1: Remove boxes[l] along with the k attached boxes of the same color
            res = (k + 1) * (k + 1) + dp(l + 1, r, 0)
            
            # Option 2: Remove boxes between l and m (where boxes[m] == boxes[l]) 
            # to merge the current group with boxes[m]
            for m in range(l + 1, r + 1):
                if boxes[m] == boxes[l]:
                    res = max(res, dp(l + 1, m - 1, 0) + dp(m, r, k + 1))
            
            memo[state] = res
            return res

        return dp(0, len(boxes) - 1, 0)