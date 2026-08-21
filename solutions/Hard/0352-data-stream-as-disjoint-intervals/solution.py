# ──────────────────────────────────────────────────
# Problem  : 352. Data Stream as Disjoint Intervals
# Difficulty: Hard
# Tags     : Hash Table, Binary Search, Union-Find, Design, Data Stream, Ordered Set
# Link     : https://leetcode.com/problems/data-stream-as-disjoint-intervals/
# Runtime  : 0 ms (beats 100%)
# Memory   : 12416000 (beats 51%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

import bisect


class SummaryRanges(object):

    def __init__(self):
        # Stores disjoint intervals in sorted order: [[start1, end1], [start2, end2], ...]
        self.intervals = []

    def addNum(self, value):
        """
        :type value: int
        :rtype: None
        """
        # Find insertion position using binary search based on start intervals
        idx = bisect.bisect_right(self.intervals, [value, float("inf")])

        # Check if value is already covered by the previous interval
        if idx > 0 and self.intervals[idx - 1][1] >= value:
            return

        # Flags to check adjacency
        connect_left = (
            idx > 0 and self.intervals[idx - 1][1] + 1 == value
        )
        connect_right = (
            idx < len(self.intervals)
            and self.intervals[idx][0] - 1 == value
        )

        if connect_left and connect_right:
            # Merges interval[idx-1] and interval[idx]
            self.intervals[idx - 1][1] = self.intervals[idx][1]
            self.intervals.pop(idx)
        elif connect_left:
            # Extends interval[idx-1] to the right
            self.intervals[idx - 1][1] = value
        elif connect_right:
            # Extends interval[idx] to the left
            self.intervals[idx][0] = value
        else:
            # Creates an isolated interval [value, value]
            self.intervals.insert(idx, [value, value])

    def getIntervals(self):
        """
        :rtype: List[List[int]]
        """
        return self.intervals