# ──────────────────────────────────────────────────
# Problem  : 834. Sum of Distances in Tree
# Difficulty: Hard
# Tags     : Dynamic Programming, Tree, Depth-First Search, Graph Theory, DP on Trees
# Link     : https://leetcode.com/problems/sum-of-distances-in-tree/
# Runtime  : 256 ms (beats 18%)
# Memory   : 61180000 (beats 40%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────





from collections import defaultdict

class Solution(object):
    def sumOfDistancesInTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        ans = [0] * n
        count = [1] * n

        def dfs_base(node, parent):
            for neighbor in graph[node]:
                if neighbor != parent:
                    dfs_base(neighbor, node)
                    count[node] += count[neighbor]
                    ans[node] += ans[neighbor] + count[neighbor]

        def dfs_reroot(node, parent):
            for neighbor in graph[node]:
                if neighbor != parent:
                    # Reroot from node to neighbor
                    ans[neighbor] = ans[node] - count[neighbor] + (n - count[neighbor])
                    dfs_reroot(neighbor, node)

        dfs_base(0, -1)
        dfs_reroot(0, -1)

        return ans