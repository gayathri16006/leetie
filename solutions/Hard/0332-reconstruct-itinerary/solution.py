# ──────────────────────────────────────────────────
# Problem  : 332. Reconstruct Itinerary
# Difficulty: Hard
# Tags     : Array, String, Depth-First Search, Graph Theory, Sorting, Heap (Priority Queue), Eulerian Circuit, Eulerian Path, Semi-Eulerian Graph
# Link     : https://leetcode.com/problems/reconstruct-itinerary/
# Runtime  : 0 ms (beats 0%)
# Memory   : 12468000 (beats 0%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

from collections import defaultdict


class Solution(object):

    def findItinerary(self, tickets):
        """
        :type tickets: List[List[int]]
        :rtype: List[str]
        """
        # Build adjacency list with reverse-sorted destinations for O(1) popping
        graph = defaultdict(list)
        for src, dst in sorted(tickets, reverse=True):
            graph[src].append(dst)

        itinerary = []

        def dfs(airport):
            while graph[airport]:
                next_airport = graph[airport].pop()
                dfs(next_airport)
            # Add to itinerary in post-order (backtrack path)
            itinerary.append(airport)

        dfs("JFK")
        # Reverse post-order traversal to get the forward Eulerian path
        return itinerary[::-1]