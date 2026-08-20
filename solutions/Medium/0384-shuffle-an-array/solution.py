# ──────────────────────────────────────────────────
# Problem  : 384. Shuffle an Array
# Difficulty: Medium
# Tags     : Array, Math, Design, Randomized
# Link     : https://leetcode.com/problems/shuffle-an-array/
# Runtime  : 72 ms (beats 16%)
# Memory   : 15748000 (beats 67%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

import random

class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.original = list(nums)
        self.array = list(nums)

    def reset(self):
        """
        :rtype: List[int]
        """
        self.array = list(self.original)
        return self.array

    def shuffle(self):
        """
        :rtype: List[int]
        """
        n = len(self.array)
        for i in range(n):
            # Pick a random index from i to n - 1
            j = random.randint(i, n - 1)
            # Swap elements
            self.array[i], self.array[j] = self.array[j], self.array[i]
            
        return self.array

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()