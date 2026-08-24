# ──────────────────────────────────────────────────
# Problem  : 528. Random Pick with Weight
# Difficulty: Medium
# Tags     : Array, Math, Binary Search, Prefix Sum, Randomized
# Link     : https://leetcode.com/problems/random-pick-with-weight/
# Runtime  : 109 ms (beats 76%)
# Memory   : 16984000 (beats 90%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

import random
import bisect

class Solution(object):

    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.prefix_sums = []
        running_sum = 0
        for weight in w:
            running_sum += weight
            self.prefix_sums.append(running_sum)
        self.total_sum = running_sum

    def pickIndex(self):
        """
        :rtype: int
        """
        # Pick a random integer in the range [1, total_sum]
        target = random.randint(1, self.total_sum)
        # Binary search to find the bucket index
        return bisect.bisect_left(self.prefix_sums, target)


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()