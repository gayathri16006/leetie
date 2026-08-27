# ──────────────────────────────────────────────────
# Problem  : 757. Set Intersection Size At Least Two
# Difficulty: Hard
# Tags     : Array, Greedy, Sorting
# Link     : https://leetcode.com/problems/set-intersection-size-at-least-two/
# Runtime  : 2 ms (beats 94%)
# Memory   : 20584000 (beats 90%)
# Language : python3
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def intersectionSizeTwo(self, intervals: list[list[int]]) -> int:
        # Sort by end time ascending, and start time descending for ties
        intervals.sort(key=lambda x: (x[1], -x[0]))
        
        # Track the two largest chosen points in the set
        p1, p2 = -1, -1
        ans = 0
        
        for start, end in intervals:
            # Case 1: Neither of the last two chosen points falls in [start, end]
            if start > p2:
                ans += 2
                p1 = end - 1
                p2 = end
            # Case 2: Only the largest chosen point falls in [start, end]
            elif start > p1:
                ans += 1
                p1 = p2
                p2 = end
            # Case 3: Both p1 and p2 are inside [start, end], no new points needed
            
        return ans