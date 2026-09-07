# ──────────────────────────────────────────────────
# Problem  : 939. Minimum Area Rectangle
# Difficulty: Medium
# Tags     : Array, Hash Table, Math, Geometry, Sorting
# Link     : https://leetcode.com/problems/minimum-area-rectangle/
# Runtime  : 950 ms (beats 77%)
# Memory   : 12472000 (beats 94%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def minAreaRect(self, points):
        point_set = set(map(tuple, points))
        ans = float('inf')

        for i in range(len(points)):
            x1, y1 = points[i]

            for j in range(i + 1, len(points)):
                x2, y2 = points[j]

                if x1 != x2 and y1 != y2:
                    if (x1, y2) in point_set and (x2, y1) in point_set:
                        area = abs(x1 - x2) * abs(y1 - y2)
                        ans = min(ans, area)

        return 0 if ans == float('inf') else ans