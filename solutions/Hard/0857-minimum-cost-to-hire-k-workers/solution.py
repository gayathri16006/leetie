# ──────────────────────────────────────────────────
# Problem  : 857. Minimum Cost to Hire K Workers
# Difficulty: Hard
# Tags     : Array, Greedy, Sorting, Heap (Priority Queue)
# Link     : https://leetcode.com/problems/minimum-cost-to-hire-k-workers/
# Runtime  : 121 ms (beats 15%)
# Memory   : 15368000 (beats 18%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

import heapq

class Solution(object):
    def mincostToHireWorkers(self, quality, wage, k):
        """
        :type quality: List[int]
        :type wage: List[int]
        :type k: int
        :rtype: float
        """
        # Pair workers and sort by wage/quality ratio
        workers = sorted([(float(w) / q, q) for w, q in zip(wage, quality)])
        
        max_heap = []
        sum_quality = 0
        min_cost = float('inf')

        for ratio, q in workers:
            heapq.heappush(max_heap, -q)
            sum_quality += q

            if len(max_heap) > k:
                # Remove the worker with the highest quality to minimize sum_quality
                sum_quality += heapq.heappop(max_heap)

            if len(max_heap) == k:
                min_cost = min(min_cost, ratio * sum_quality)

        return min_cost