# ──────────────────────────────────────────────────
# Problem  : 295. Find Median from Data Stream
# Difficulty: Hard
# Tags     : Two Pointers, Design, Sorting, Heap (Priority Queue), Data Stream
# Link     : https://leetcode.com/problems/find-median-from-data-stream/
# Runtime  : 721 ms (beats 62%)
# Memory   : 35804000 (beats 25%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

import heapq


class MedianFinder(object):

    def __init__(self):
        # max_heap stores the smaller half of numbers (inverted values for Python min-heap)
        self.small = []
        # min_heap stores the larger half of numbers
        self.large = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        # Always push to max-heap first (as negative number)
        heapq.heappush(self.small, -num)

        # Ensure every element in small is <= every element in large
        if self.small and self.large and (-self.small[0] > self.large[0]):
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        # Balance the sizes: len(small) can be at most len(large) + 1
        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        elif len(self.large) > len(self.small):
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)

    def findMedian(self):
        """
        :rtype: float
        """
        # If odd number of elements, the root of the larger heap (small) is the median
        if len(self.small) > len(self.large):
            return float(-self.small[0])

        # If even, median is the average of the tops of both heaps
        return (-self.small[0] + self.large[0]) / 2.0