# ──────────────────────────────────────────────────
# Problem  : 478. Generate Random Point in a Circle
# Difficulty: Medium
# Tags     : Math, Geometry, Rejection Sampling, Randomized
# Link     : https://leetcode.com/problems/generate-random-point-in-a-circle/
# Runtime  : 0 ms (beats 0%)
# Memory   : 12556000 (beats 0%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

import math
import random

class Solution(object):

    def __init__(self, radius, x_center, y_center):
        """
        :type radius: float
        :type x_center: float
        :type y_center: float
        """
        self.radius = radius
        self.x_center = x_center
        self.y_center = y_center

    def randPoint(self):
        """
        :rtype: List[float]
        """
        # Uniform angle from 0 to 2*pi
        theta = random.uniform(0, 2 * math.pi)
        
        # Square root is required so points don't cluster at the center
        r = math.sqrt(random.uniform(0, 1)) * self.radius
        
        x = self.x_center + r * math.cos(theta)
        y = self.y_center + r * math.sin(theta)
        
        return [x, y]