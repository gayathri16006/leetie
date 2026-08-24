# ──────────────────────────────────────────────────
# Problem  : 593. Valid Square
# Difficulty: Medium
# Tags     : Math, Geometry
# Link     : https://leetcode.com/problems/valid-square/
# Runtime  : 0 ms (beats 100%)
# Memory   : 12492000 (beats 25%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        def dist_sq(a, b):
            return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2

        points = [p1, p2, p3, p4]
        distances = []

        # Calculate all 6 pairwise squared distances
        for i in range(4):
            for j in range(i + 1, 4):
                distances.append(dist_sq(points[i], points[j]))

        distances.sort()

        # For a valid square:
        # 1. The smallest distance > 0 (points must not overlap)
        # 2. 4 equal side lengths (distances[0..3])
        # 3. 2 equal diagonal lengths (distances[4..5])
        return (
            distances[0] > 0 and
            distances[0] == distances[1] == distances[2] == distances[3] and
            distances[4] == distances[5]
        )