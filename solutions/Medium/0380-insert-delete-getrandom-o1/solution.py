# ──────────────────────────────────────────────────
# Problem  : 380. Insert Delete GetRandom O(1)
# Difficulty: Medium
# Tags     : Array, Hash Table, Math, Design, Randomized
# Link     : https://leetcode.com/problems/insert-delete-getrandom-o1/
# Runtime  : 0 ms (beats 0%)
# Memory   : 12280000 (beats 0%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

import random

class RandomizedSet(object):

    def __init__(self):
        self.val_to_index = {}
        self.nums = []

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.val_to_index:
            return False
        
        self.val_to_index[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.val_to_index:
            return False
        
        # Swap the element to remove with the last element in the list
        idx = self.val_to_index[val]
        last_element = self.nums[-1]
        
        self.nums[idx] = last_element
        self.val_to_index[last_element] = idx
        
        # Pop the last element from both structures
        self.nums.pop()
        del self.val_to_index[val]
        
        return True

    def getRandom(self):
        """
        :rtype: int
        """
        return random.choice(self.nums)