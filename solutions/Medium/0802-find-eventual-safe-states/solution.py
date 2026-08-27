# ──────────────────────────────────────────────────
# Problem  : 802. Find Eventual Safe States
# Difficulty: Medium
# Tags     : Depth-First Search, Breadth-First Search, Graph Theory, Topological Sort, Kosaraju's Algorithm, Tarjan's SCC Algorithm
# Link     : https://leetcode.com/problems/find-eventual-safe-states/
# Runtime  : 18 ms (beats 96%)
# Memory   : 27444000 (beats 47%)
# Language : python3
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def eventualSafeNodes(self, graph: list[list[int]]) -> list[int]:
        n = len(graph)
        # State: 0 = unvisited, 1 = visiting (in recursion stack / cycle), 2 = safe
        state = [0] * n
        
        def is_safe(node: int) -> bool:
            if state[node] > 0:
                return state[node] == 2
            
            # Mark as visiting
            state[node] = 1
            
            for neighbor in graph[node]:
                if not is_safe(neighbor):
                    return False
                    
            # Mark as safe after all outgoing paths lead to terminal nodes
            state[node] = 2
            return True
            
        return [i for i in range(n) if is_safe(i)]