# ──────────────────────────────────────────────────
# Problem  : 390. Elimination Game
# Difficulty: Medium
# Tags     : Math, Recursion
# Link     : https://leetcode.com/problems/elimination-game/
# Runtime  : 0 ms (beats 0%)
# Memory   : 12528000 (beats 0%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        head = 1
        step = 1
        remaining = n
        left_to_right = True
        
        while remaining > 1:
            # The head always changes when moving left-to-right,
            # or when moving right-to-left if the total count is odd.
            if left_to_right or remaining % 2 == 1:
                head += step
                
            remaining //= 2
            step *= 2
            left_to_right = not left_to_right
            
        return head