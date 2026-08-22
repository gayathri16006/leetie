# ──────────────────────────────────────────────────
# Problem  : 502. IPO
# Difficulty: Hard
# Tags     : Array, Greedy, Sorting, Heap (Priority Queue)
# Link     : https://leetcode.com/problems/ipo/
# Runtime  : 0 ms (beats 0%)
# Memory   : 12168000 (beats 0%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

import heapq

class Solution(object):
    def findMaximizedCapital(self, k, w, profits, capital):
        """
        :type k: int
        :type w: int
        :type profits: List[int]
        :type capital: List[int]
        :rtype: int
        """
        # Pair capital and profit, then sort ascending by required capital
        projects = sorted(zip(capital, profits))
        n = len(projects)
        max_profit_heap = []
        i = 0

        # Perform up to k project selections
        for _ in range(k):
            # Push all available projects that can be afforded with current capital w
            while i < n and projects[i][0] <= w:
                # Python min-heap stores negative values to simulate a max-heap
                heapq.heappush(max_profit_heap, -projects[i][1])
                i += 1

            # If no affordable projects remain, stop early
            if not max_profit_heap:
                break

            # Choose the most profitable project available
            w += -heapq.heappop(max_profit_heap)

        return w