# ──────────────────────────────────────────────────
# Problem  : 435. Non-overlapping Intervals
# Difficulty: Medium
# Tags     : Array, Dynamic Programming, Greedy, Sorting
# Link     : https://leetcode.com/problems/non-overlapping-intervals/
# Runtime  : 0 ms (beats 0%)
# Memory   : 12480000 (beats 0%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if not intervals:
            return 0

        # Sort intervals by their end time
        intervals.sort(key=lambda x: x[1])

        removals = 0
        prev_end = intervals[0][1]

        for i in range(1, len(intervals)):
            start, end = intervals[i]
            # If current interval overlaps with previous interval's end
            if start < prev_end:
                removals += 1
            else:
                # No overlap; update the end boundary
                prev_end = end

        return removals