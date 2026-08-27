# ──────────────────────────────────────────────────
# Problem  : 753. Cracking the Safe
# Difficulty: Hard
# Tags     : String, Depth-First Search, Graph Theory, Eulerian Circuit, Eulerian Path, Eulerian Graph
# Link     : https://leetcode.com/problems/cracking-the-safe/
# Runtime  : 0 ms (beats 0%)
# Memory   : 19240000 (beats 0%)
# Language : python3
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        if n == 1:
            return "".join(str(i) for i in range(k))
        
        visited = set()
        result = []
        
        # Start node represents a prefix of length n - 1
        start_node = "0" * (n - 1)
        
        # Hierholzer's Algorithm for Eulerian circuit on De Bruijn graph
        def dfs(node: str):
            for x in range(k):
                edge = node + str(x)
                if edge not in visited:
                    visited.add(edge)
                    dfs(edge[1:])
                    result.append(str(x))
                    
        dfs(start_node)
        return "".join(result) + start_node