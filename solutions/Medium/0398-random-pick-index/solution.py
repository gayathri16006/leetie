# ──────────────────────────────────────────────────
# Problem  : 398. Random Pick Index
# Difficulty: Medium
# Tags     : Hash Table, Math, Reservoir Sampling, Randomized
# Link     : https://leetcode.com/problems/random-pick-index/
# Runtime  : 71 ms (beats 53%)
# Memory   : 23272000 (beats 68%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

import random
from collections import defaultdict


class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.indices = defaultdict(list)
        for i, num in enumerate(nums):
            self.indices[num].append(i)

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        return random.choice(self.indices[target])