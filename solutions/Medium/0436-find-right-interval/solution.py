# ──────────────────────────────────────────────────
# Problem  : 436. Find Right Interval
# Difficulty: Medium
# Tags     : Array, Binary Search, Sorting
# Link     : https://leetcode.com/problems/find-right-interval/
# Runtime  : 35 ms (beats 77%)
# Memory   : 16552000 (beats 83%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

import bisect

class Solution(object):
    def findRightInterval(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[int]
        """
        n = len(intervals)
        
        # Store (start_time, original_index) and sort by start_time
        starts = sorted((interval[0], i) for i, interval in enumerate(intervals))
        
        result = []
        for interval in intervals:
            end = interval[1]
            # Binary search for the smallest start >= current interval's end
            idx = bisect.bisect_left(starts, (end,))
            
            if idx < n:
                result.append(starts[idx][1])
            else:
                result.append(-1)
                
        return result