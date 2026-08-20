# ──────────────────────────────────────────────────
# Problem  : 399. Evaluate Division
# Difficulty: Medium
# Tags     : Array, String, Depth-First Search, Breadth-First Search, Union-Find, Graph Theory, Shortest Path, Bellman–Ford Algorithm, Floyd–Warshall Algorithm
# Link     : https://leetcode.com/problems/evaluate-division/
# Runtime  : 0 ms (beats 0%)
# Memory   : 12540000 (beats 0%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

from collections import defaultdict

class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        # Step 1: Build the graph
        graph = defaultdict(dict)
        for (u, v), val in zip(equations, values):
            graph[u][v] = val
            graph[v][u] = 1.0 / val

        # Step 2: DFS function to find path product from src to dst
        def dfs(src, dst, visited):
            if src not in graph or dst not in graph:
                return -1.0
            if src == dst:
                return 1.0
            
            visited.add(src)
            for neighbor, weight in graph[src].items():
                if neighbor not in visited:
                    prod = dfs(neighbor, dst, visited)
                    if prod != -1.0:
                        return weight * prod
            return -1.0

        # Step 3: Process all queries
        results = []
        for src, dst in queries:
            results.append(dfs(src, dst, set()))
            
        return results