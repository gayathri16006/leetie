# ──────────────────────────────────────────────────
# Problem  : 715. Range Module
# Difficulty: Hard
# Tags     : Design, Segment Tree, Ordered Set
# Link     : https://leetcode.com/problems/range-module/
# Runtime  : 88 ms (beats 90%)
# Memory   : 16324000 (beats 35%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

import bisect

class RangeModule(object):

    def __init__(self):
        # Stores alternating endpoints: [start_0, end_0, start_1, end_1, ...]
        self.intervals = []

    def addRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: None
        """
        i = bisect.bisect_left(self.intervals, left)
        j = bisect.bisect_right(self.intervals, right)
        
        sub = []
        if i % 2 == 0:
            sub.append(left)
        if j % 2 == 0:
            sub.append(right)
            
        self.intervals[i:j] = sub

    def queryRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: bool
        """
        i = bisect.bisect_right(self.intervals, left)
        j = bisect.bisect_left(self.intervals, right)
        
        # Must fall completely inside a single interval (odd index)
        return i == j and i % 2 == 1

    def removeRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: None
        """
        i = bisect.bisect_left(self.intervals, left)
        j = bisect.bisect_right(self.intervals, right)
        
        sub = []
        if i % 2 == 1:
            sub.append(left)
        if j % 2 == 1:
            sub.append(right)
            
        self.intervals[i:j] = sub