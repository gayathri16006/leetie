# ──────────────────────────────────────────────────
# Problem  : 963. Minimum Area Rectangle II
# Difficulty: Medium
# Tags     : Array, Hash Table, Math, Geometry
# Link     : https://leetcode.com/problems/minimum-area-rectangle-ii/
# Runtime  : 0 ms (beats 0%)
# Memory   : 12296000 (beats 0%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

import collections
import math

class Solution(object):
    def minAreaFreeRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        n = len(points)
        # Group pairs of points by (squared diagonal distance, midpoint)
        # Diagonals of a rectangle are equal in length and share the same midpoint
        groups = collections.defaultdict(list)
        
        for i in range(n):
            p1 = points[i]
            for j in range(i + 1, n):
                p2 = points[j]
                dist_sq = (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2
                midpoint = (p1[0] + p2[0], p1[1] + p2[1])
                groups[(dist_sq, midpoint)].append((p1, p2))
                
        min_area = float('inf')
        
        for (dist_sq, midpoint), pairs in groups.items():
            if len(pairs) < 2:
                continue
            for i in range(len(pairs)):
                p1, p2 = pairs[i]
                for j in range(i + 1, len(pairs)):
                    p3, p4 = pairs[j]
                    
                    d1 = math.hypot(p1[0] - p3[0], p1[1] - p3[1])
                    d2 = math.hypot(p1[0] - p4[0], p1[1] - p4[1])
                    min_area = min(min_area, d1 * d2)
                    
        return float(min_area) if min_area != float('inf') else 0.0