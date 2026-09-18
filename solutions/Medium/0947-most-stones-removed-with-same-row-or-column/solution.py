# ──────────────────────────────────────────────────
# Problem  : 947. Most Stones Removed with Same Row or Column
# Difficulty: Medium
# Tags     : Hash Table, Depth-First Search, Union-Find, Graph Theory, Bipartite Graph
# Link     : https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/
# Runtime  : 21 ms (beats 90%)
# Memory   : 12856000 (beats 70%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def removeStones(self, stones):
        """
        :type stones: List[List[int]]
        :rtype: int
        """
        parent = {}

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            root_x = find(x)
            root_y = find(y)
            if root_x != root_y:
                parent[root_x] = root_y

        for r, c in stones:
            # Distinguish row coordinates from column coordinates using ~c
            col_id = ~c
            if r not in parent:
                parent[r] = r
            if col_id not in parent:
                parent[col_id] = col_id
            union(r, col_id)

        
        num_components = len({find(x) for x in parent})

        
        return len(stones) - num_components