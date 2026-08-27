# ──────────────────────────────────────────────────
# Problem  : 710. Random Pick with Blacklist
# Difficulty: Hard
# Tags     : Array, Hash Table, Math, Binary Search, Sorting, Randomized
# Link     : https://leetcode.com/problems/random-pick-with-blacklist/
# Runtime  : 152 ms (beats 49%)
# Memory   : 21496000 (beats 72%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

import random

class Solution(object):

    def __init__(self, n, blacklist):
        """
        :type n: int
        :type blacklist: List[int]
        """
        self.valid_size = n - len(blacklist)
        self.mapping = {}
        
        # Numbers in the upper range [valid_size, n - 1] that are in blacklist
        black_set = set(blacklist)
        
        # Pointer to find available valid numbers from the top [valid_size, n - 1]
        last = n - 1
        for b in blacklist:
            # We only need to remap blacklisted numbers that fall in [0, valid_size - 1]
            if b < self.valid_size:
                # Find the next available non-blacklisted number from the top
                while last in black_set:
                    last -= 1
                self.mapping[b] = last
                last -= 1

    def pick(self):
        """
        :rtype: int
        """
        # Pick uniformly from [0, valid_size - 1]
        idx = random.randint(0, self.valid_size - 1)
        # If it's mapped (was blacklisted), return the remapped valid number
        return self.mapping.get(idx, idx)