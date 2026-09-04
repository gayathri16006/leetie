# ──────────────────────────────────────────────────
# Problem  : 847. Shortest Path Visiting All Nodes
# Difficulty: Hard
# Tags     : Dynamic Programming, Bit Manipulation, Breadth-First Search, Graph Theory, Bitmask
# Link     : https://leetcode.com/problems/shortest-path-visiting-all-nodes/
# Runtime  : 125 ms (beats 40%)
# Memory   : 17508000 (beats 79%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

from collections import deque

class Solution(object):
    def shortestPathLength(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: int
        """
        n = len(graph)
        if n <= 1:
            return 0

        target_mask = (1 << n) - 1
        queue = deque()
        visited = set()

        # Multi-source initialization: start from each node
        for i in range(n):
            mask = 1 << i
            queue.append((i, mask, 0))
            visited.add((i, mask))

        while queue:
            node, mask, dist = queue.popleft()

            for neighbor in graph[node]:
                next_mask = mask | (1 << neighbor)

                if next_mask == target_mask:
                    return dist + 1

                if (neighbor, next_mask) not in visited:
                    visited.add((neighbor, next_mask))
                    queue.append((neighbor, next_mask, dist + 1))

        return 0