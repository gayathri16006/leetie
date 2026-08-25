# ──────────────────────────────────────────────────
# Problem  : 685. Redundant Connection II
# Difficulty: Hard
# Tags     : Depth-First Search, Breadth-First Search, Union-Find, Graph Theory
# Link     : https://leetcode.com/problems/redundant-connection-ii/
# Runtime  : 3 ms (beats 59%)
# Memory   : 19680000 (beats 55%)
# Language : python3
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

from typing import List

class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = {}
        candidate1 = None
        candidate2 = None
        
        # Step 1: Check if any node has two parents (in-degree == 2)
        for u, v in edges:
            if v in parent:
                candidate1 = [parent[v], v]  # First incoming edge to v
                candidate2 = [u, v]          # Second incoming edge to v
                break
            parent[v] = u
            
        # Step 2: Union-Find to detect cycles
        dsu = list(range(n + 1))
        
        def find(x: int) -> int:
            if dsu[x] != x:
                dsu[x] = find(dsu[x])
            return dsu[x]
        
        def union(x: int, y: int) -> bool:
            rx, ry = find(x), find(y)
            if rx == ry:
                return False
            dsu[rx] = ry
            return True
            
        for u, v in edges:
            # Skip the second edge leading to the two-parent node
            if candidate2 and [u, v] == candidate2:
                continue
            if not union(u, v):
                # Cycle detected
                if candidate1:
                    # If there was a two-parent conflict, candidate1 is the culprit
                    return candidate1
                # Otherwise, this edge creates the directed cycle
                return [u, v]
                
        # If no cycle was detected after skipping candidate2, candidate2 was the culprit
        return candidate2