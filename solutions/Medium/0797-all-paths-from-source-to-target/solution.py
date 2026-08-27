# ──────────────────────────────────────────────────
# Problem  : 797. All Paths From Source to Target
# Difficulty: Medium
# Tags     : Backtracking, Depth-First Search, Breadth-First Search, Graph Theory, Directed Acyclic Graph
# Link     : https://leetcode.com/problems/all-paths-from-source-to-target/
# Runtime  : 5 ms (beats 52%)
# Memory   : 20600000 (beats 51%)
# Language : python3
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:
        target = len(graph) - 1
        result = []
        
        def dfs(node: int, path: list[int]):
            if node == target:
                result.append(list(path))
                return
            
            for neighbor in graph[node]:
                path.append(neighbor)
                dfs(neighbor, path)
                path.pop()  # Backtrack
                
        dfs(0, [0])
        return result