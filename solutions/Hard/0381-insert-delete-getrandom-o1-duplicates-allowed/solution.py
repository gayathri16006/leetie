# ──────────────────────────────────────────────────
# Problem  : 381. Insert Delete GetRandom O(1) - Duplicates allowed
# Difficulty: Hard
# Tags     : Array, Hash Table, Math, Design, Randomized
# Link     : https://leetcode.com/problems/insert-delete-getrandom-o1-duplicates-allowed/
# Runtime  : 199 ms (beats 44%)
# Memory   : 67300000 (beats 35%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

import random
from collections import defaultdict


class RandomizedCollection(object):

    def __init__(self):
        # List of elements to support O(1) random access
        self.nums = []
        # Mapping: val -> set of indices where val occurs in self.nums
        self.idx_map = defaultdict(set)

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        # True if val was not already present
        is_not_present = len(self.idx_map[val]) == 0

        self.idx_map[val].add(len(self.nums))
        self.nums.append(val)

        return is_not_present

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if not self.idx_map[val]:
            return False

        # Get an index of the element to remove
        remove_idx = self.idx_map[val].pop()
        last_val = self.nums[-1]
        last_idx = len(self.nums) - 1

        # Swap with the last element if not removing the last element directly
        if remove_idx != last_idx:
            self.nums[remove_idx] = last_val
            # Update the index mapping for the swapped last element
            self.idx_map[last_val].remove(last_idx)
            self.idx_map[last_val].add(remove_idx)

        # Remove the last element from the array
        self.nums.pop()

        return True

    def getRandom(self):
        """
        :rtype: int
        """
        return random.choice(self.nums)