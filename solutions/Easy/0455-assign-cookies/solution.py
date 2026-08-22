# ──────────────────────────────────────────────────
# Problem  : 455. Assign Cookies
# Difficulty: Easy
# Tags     : Array, Two Pointers, Greedy, Sorting, Quicksort
# Link     : https://leetcode.com/problems/assign-cookies/
# Runtime  : 0 ms (beats 0%)
# Memory   : 12228000 (beats 0%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        
        child_i = 0
        cookie_j = 0
        
        # Try to satisfy the least greedy child with the smallest possible cookie
        while child_i < len(g) and cookie_j < len(s):
            if s[cookie_j] >= g[child_i]:
                child_i += 1
            cookie_j += 1
            
        return child_i