# ──────────────────────────────────────────────────
# Problem  : 519. Random Flip Matrix
# Difficulty: Medium
# Tags     : Hash Table, Math, Reservoir Sampling, Randomized
# Link     : https://leetcode.com/problems/random-flip-matrix/
# Runtime  : 0 ms (beats 0%)
# Memory   : 12464000 (beats 0%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

import random

class Solution(object):

    def __init__(self, m, n):
        """
        :type m: int
        :type n: int
        """
        self.m = m
        self.n = n
        self.total = m * n
        self.map = {}

    def flip(self):
        """
        :rtype: List[int]
        """
        self.total -= 1
        # Pick a random candidate from remaining unused pool
        r = random.randint(0, self.total)
        
        # Look up mapped original index for r, fallback to r
        idx = self.map.get(r, r)
        
        # Swap chosen slot with the current tail
        self.map[r] = self.map.get(self.total, self.total)
        
        # Convert 1D index back to 2D matrix coordinates (row, col)
        return [idx // self.n, idx % self.n]

    def reset(self):
        """
        :rtype: None
        """
        self.map.clear()
        self.total = self.m * self.n


# Your Solution object will be instantiated and called as such:
# obj = Solution(m, n)
# param_1 = obj.flip()
# obj.reset()