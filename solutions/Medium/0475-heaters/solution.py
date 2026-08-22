# ──────────────────────────────────────────────────
# Problem  : 475. Heaters
# Difficulty: Medium
# Tags     : Array, Two Pointers, Binary Search, Sorting
# Link     : https://leetcode.com/problems/heaters/
# Runtime  : 0 ms (beats 0%)
# Memory   : 12208000 (beats 0%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

import bisect

class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        heaters.sort()
        max_radius = 0
        n = len(heaters)

        for house in houses:
            # Find insertion point for the house in sorted heaters
            idx = bisect.bisect_left(heaters, house)
            
            # Distance to the heater on the right (if it exists)
            dist_right = heaters[idx] - house if idx < n else float('inf')
            
            # Distance to the heater on the left (if it exists)
            dist_left = house - heaters[idx - 1] if idx > 0 else float('inf')
            
            # The house will be warmed by the closer heater
            closest_dist = min(dist_left, dist_right)
            
            # The global radius must cover the most isolated house
            max_radius = max(max_radius, closest_dist)

        return max_radius