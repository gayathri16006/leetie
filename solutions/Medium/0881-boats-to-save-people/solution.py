# ──────────────────────────────────────────────────
# Problem  : 881. Boats to Save People
# Difficulty: Medium
# Tags     : Array, Two Pointers, Greedy, Sorting, Timsort
# Link     : https://leetcode.com/problems/boats-to-save-people/
# Runtime  : 74 ms (beats 24%)
# Memory   : 16424000 (beats 54%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people.sort()
        left = 0
        right = len(people) - 1
        boats = 0

        while left <= right:
            # If the lightest and heaviest person can share a boat
            if people[left] + people[right] <= limit:
                left += 1
            
            # The heaviest person always takes a boat
            right -= 1
            boats += 1

        return boats