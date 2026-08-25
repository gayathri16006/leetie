# ──────────────────────────────────────────────────
# Problem  : 684. Redundant Connection
# Difficulty: Medium
# Tags     : Depth-First Search, Breadth-First Search, Union-Find, Graph Theory
# Link     : https://leetcode.com/problems/redundant-connection/
# Runtime  : 0 ms (beats 0%)
# Memory   : 19388000 (beats 0%)
# Language : python3
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

from typing import List

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = list(range(n + 1))
        rank = [1] * (n + 1)
        
        def find(x: int) -> int:
            if parent[x] != x:
                parent[x] = find(parent[x])  # Path compression
            return parent[x]
        
        def union(x: int, y: int) -> bool:
            root_x, root_y = find(x), find(y)
            
            # If both nodes already share the same root, an edge between them creates a cycle
            if root_x == root_y:
                return False
            
            # Union by rank
            if rank[root_x] < rank[root_y]:
                parent[root_x] = root_y
            elif rank[root_x] > rank[root_y]:
                parent[root_y] = root_x
            else:
                parent[root_y] = root_x
                rank[root_x] += 1
                
            return True

        for u, v in edges:
            if not union(u, v):
                return [u, v]
                
        return []