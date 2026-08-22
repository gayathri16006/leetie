# ──────────────────────────────────────────────────
# Problem  : 473. Matchsticks to Square
# Difficulty: Medium
# Tags     : Array, Dynamic Programming, Backtracking, Bit Manipulation, Bitmask
# Link     : https://leetcode.com/problems/matchsticks-to-square/
# Runtime  : 0 ms (beats 0%)
# Memory   : 12468000 (beats 0%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def makesquare(self, matchsticks):
        """
        :type matchsticks: List[int]
        :rtype: bool
        """
        total_len = sum(matchsticks)
        
        # A valid square must be divisible into 4 equal sides
        if total_len % 4 != 0 or len(matchsticks) < 4:
            return False
        
        target = total_len // 4
        
        # Sort in descending order to hit invalid paths early
        matchsticks.sort(reverse=True)
        
        # If any single matchstick exceeds target side length
        if matchsticks[0] > target:
            return False
        
        sides = [0] * 4
        
        def backtrack(index):
            if index == len(matchsticks):
                return True
            
            val = matchsticks[index]
            for i in range(4):
                if sides[i] + val <= target:
                    sides[i] += val
                    if backtrack(index + 1):
                        return True
                    sides[i] -= val
                
                # Pruning: If a matchstick doesn't fit in an empty side,
                # trying it in subsequent empty sides is redundant.
                if sides[i] == 0:
                    break
                    
            return False
        
        return backtrack(0)