# ──────────────────────────────────────────────────
# Problem  : 882. Reachable Nodes In Subdivided Graph
# Difficulty: Hard
# Tags     : Graph Theory, Heap (Priority Queue), Shortest Path, Dijkstra's Algorithm
# Link     : https://leetcode.com/problems/reachable-nodes-in-subdivided-graph/
# Runtime  : 0 ms (beats 0%)
# Memory   : 12460000 (beats 0%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

import heapq
from collections import defaultdict

class Solution(object):
    def reachableNodes(self, edges, maxMoves, n):
        """
        :type edges: List[List[int]]
        :type maxMoves: int
        :type n: int
        :rtype: int
        """
        graph = defaultdict(dict)
        for u, v, cnt in edges:
            graph[u][v] = cnt
            graph[v][u] = cnt

        # Step 1: Dijkstra's to find shortest paths from node 0
        dist = {}
        pq = [(0, 0)]  # (distance, node)

        while pq:
            d, u = heapq.heappop(pq)
            if u in dist:
                continue
            dist[u] = d

            for v, cnt in graph[u].items():
                if v not in dist and d + cnt + 1 <= maxMoves:
                    heapq.heappush(pq, (d + cnt + 1, v))

        # Count reachable original nodes
        ans = len(dist)

        # Step 2: Count reachable subdivided nodes along each edge
        for u, v, cnt in edges:
            reach_u = max(0, maxMoves - dist[u]) if u in dist else 0
            reach_v = max(0, maxMoves - dist[v]) if v in dist else 0
            ans += min(cnt, reach_u + reach_v)

        return ans