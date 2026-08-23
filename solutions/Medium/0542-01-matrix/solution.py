# ──────────────────────────────────────────────────
# Problem  : 542. 01 Matrix
# Difficulty: Medium
# Tags     : Array, Dynamic Programming, Breadth-First Search, Matrix
# Link     : https://leetcode.com/problems/01-matrix/
# Runtime  : 174 ms (beats 63%)
# Memory   : 15764000 (beats 56%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

from collections import deque

class Solution(object):
    def updateMatrix(self, mat):
        m, n = len(mat), len(mat[0])
        dist = [[-1] * n for _ in range(m)]
        queue = deque()
        
        # Initialize queue with all 0s
        for r in range(m):
            for c in range(n):
                if mat[r][c] == 0:
                    dist[r][c] = 0
                    queue.append((r, c))
                    
        # 4-directional offsets
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        while queue:
            r, c = queue.popleft()
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                # If neighbor is within bounds and unvisited
                if 0 <= nr < m and 0 <= nc < n and dist[nr][nc] == -1:
                    dist[nr][nc] = dist[r][c] + 1
                    queue.append((nr, nc))
                    
        return dist