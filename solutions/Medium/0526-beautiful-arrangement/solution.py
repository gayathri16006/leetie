# ──────────────────────────────────────────────────
# Problem  : 526. Beautiful Arrangement
# Difficulty: Medium
# Tags     : Array, Dynamic Programming, Backtracking, Bit Manipulation, Bitmask
# Link     : https://leetcode.com/problems/beautiful-arrangement/
# Runtime  : 0 ms (beats 0%)
# Memory   : 12396000 (beats 0%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def countArrangement(self, n):
        """
        :type n: int
        :rtype: int
        """
        visited = [False] * (n + 1)
        
        def backtrack(pos):
            # Base case: successfully placed all numbers from n down to 1
            if pos == 0:
                return 1
            
            count = 0
            for num in range(1, n + 1):
                if not visited[num] and (num % pos == 0 or pos % num == 0):
                    visited[num] = True
                    count += backtrack(pos - 1)
                    visited[num] = False
                    
            return count

        return backtrack(n)