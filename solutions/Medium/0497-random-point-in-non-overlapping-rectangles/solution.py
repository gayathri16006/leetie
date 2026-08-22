# ──────────────────────────────────────────────────
# Problem  : 497. Random Point in Non-overlapping Rectangles
# Difficulty: Medium
# Tags     : Array, Math, Binary Search, Reservoir Sampling, Prefix Sum, Ordered Set, Randomized
# Link     : https://leetcode.com/problems/random-point-in-non-overlapping-rectangles/
# Runtime  : 98 ms (beats 28%)
# Memory   : 16004000 (beats 55%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

import random
import bisect

class Solution(object):

    def __init__(self, rects):
        """
        :type rects: List[List[int]]
        """
        self.rects = rects
        self.prefix_sums = []
        current_sum = 0
        
        for x1, y1, x2, y2 in rects:
            # Number of points is (width + 1) * (height + 1)
            num_points = (x2 - x1 + 1) * (y2 - y1 + 1)
            current_sum += num_points
            self.prefix_sums.append(current_sum)
            
        self.total_points = current_sum

    def pick(self):
        """
        :rtype: List[int]
        """
        # 1. Pick a random target point index across all rectangles
        target = random.randint(1, self.total_points)
        
        # 2. Find which rectangle contains this target point using binary search
        rect_idx = bisect.bisect_left(self.prefix_sums, target)
        x1, y1, x2, y2 = self.rects[rect_idx]
        
        # 3. Pick a random x and y uniformly within the chosen rectangle
        return [random.randint(x1, x2), random.randint(y1, y2)]