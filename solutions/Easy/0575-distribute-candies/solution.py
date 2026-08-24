# ──────────────────────────────────────────────────
# Problem  : 575. Distribute Candies
# Difficulty: Easy
# Tags     : Array, Hash Table
# Link     : https://leetcode.com/problems/distribute-candies/
# Runtime  : 0 ms (beats 0%)
# Memory   : 12276000 (beats 0%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def distributeCandies(self, candyType):
        """
        :type candyType: List[int]
        :rtype: int
        """
        unique_types = len(set(candyType))
        max_allowed = len(candyType) // 2
        
        return min(unique_types, max_allowed)