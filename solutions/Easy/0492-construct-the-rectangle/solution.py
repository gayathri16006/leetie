# ──────────────────────────────────────────────────
# Problem  : 492. Construct the Rectangle
# Difficulty: Easy
# Tags     : Math
# Link     : https://leetcode.com/problems/construct-the-rectangle/
# Runtime  : 0 ms (beats 0%)
# Memory   : 12364000 (beats 0%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

import math


class Solution(object):

    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        # Start searching for width W from floor(sqrt(area)) down to 1
        w = int(math.sqrt(area))

        while area % w != 0:
            w -= 1

        return [area // w, w]