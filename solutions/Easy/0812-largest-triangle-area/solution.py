# ──────────────────────────────────────────────────
# Problem  : 812. Largest Triangle Area
# Difficulty: Easy
# Tags     : Array, Math, Geometry, Polygons
# Link     : https://leetcode.com/problems/largest-triangle-area/
# Runtime  : 55 ms (beats 53%)
# Memory   : 12252000 (beats 92%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

import itertools

class Solution(object):
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        def area(p1, p2, p3):
            return 0.5 * abs(
                p1[0] * (p2[1] - p3[1]) +
                p2[0] * (p3[1] - p1[1]) +
                p3[0] * (p1[1] - p2[1])
            )

        return max(area(p1, p2, p3) for p1, p2, p3 in itertools.combinations(points, 3))