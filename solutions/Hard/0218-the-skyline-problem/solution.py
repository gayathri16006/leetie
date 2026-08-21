# ──────────────────────────────────────────────────
# Problem  : 218. The Skyline Problem
# Difficulty: Hard
# Tags     : Array, Divide and Conquer, Binary Indexed Tree, Segment Tree, Sweep Line, Sorting, Heap (Priority Queue), Ordered Set
# Link     : https://leetcode.com/problems/the-skyline-problem/
# Runtime  : 51 ms (beats 18%)
# Memory   : 21236000 (beats 54%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

import heapq


class Solution(object):

    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        # Collect critical points (events)
        # Start of building: (L, -H, R) -> negative height ensures taller buildings are processed first
        # End of building: (R, 0, 0)
        events = []
        for L, R, H in buildings:
            events.append((L, -H, R))
            events.append((R, 0, 0))

        # Sort events primarily by x-coordinate, then by height
        events.sort()

        # Max-heap storing pairs of (-height, right_boundary)
        # Initialize with ground level (height 0, infinity boundary)
        max_heap = [(0, float("inf"))]
        result = []

        for x, neg_h, r in events:
            # If entering a new building, push its (-height, right_boundary)
            if neg_h != 0:
                heapq.heappush(max_heap, (neg_h, r))

            # Lazily remove buildings from top of heap that have already ended at or before current x
            while max_heap[0][1] <= x:
                heapq.heappop(max_heap)

            # Current active maximum height
            curr_max_h = -max_heap[0][0]

            # If the max height changes, record this critical point
            if not result or result[-1][1] != curr_max_h:
                result.append([x, curr_max_h])

        return result