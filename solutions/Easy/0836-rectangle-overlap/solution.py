# ──────────────────────────────────────────────────
# Problem  : 836. Rectangle Overlap
# Difficulty: Easy
# Tags     : Math, Geometry
# Link     : https://leetcode.com/problems/rectangle-overlap/
# Runtime  : 3 ms (beats 0%)
# Memory   : 12400000 (beats 53%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        # Check horizontal and vertical overlaps
        overlap_x = rec1[0] < rec2[2] and rec2[0] < rec1[2]
        overlap_y = rec1[1] < rec2[3] and rec2[1] < rec1[3]

        return overlap_x and overlap_y