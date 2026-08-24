# ──────────────────────────────────────────────────
# Problem  : 547. Number of Provinces
# Difficulty: Medium
# Tags     : Depth-First Search, Breadth-First Search, Union-Find, Graph Theory
# Link     : https://leetcode.com/problems/number-of-provinces/
# Runtime  : 4 ms (beats 89%)
# Memory   : 13468000 (beats 48%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        n = len(isConnected)
        visited = [False] * n
        provinces = 0
        
        def dfs(city):
            visited[city] = True
            for neighbor in range(n):
                if isConnected[city][neighbor] == 1 and not visited[neighbor]:
                    dfs(neighbor)
                    
        for i in range(n):
            if not visited[i]:
                dfs(i)
                provinces += 1
                
        return provinces