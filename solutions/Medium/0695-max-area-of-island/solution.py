# ──────────────────────────────────────────────────
# Problem  : 695. Max Area of Island
# Difficulty: Medium
# Tags     : Array, Depth-First Search, Breadth-First Search, Union-Find, Matrix
# Link     : https://leetcode.com/problems/max-area-of-island/
# Runtime  : 19 ms (beats 62%)
# Memory   : 20512000 (beats 53%)
# Language : python3
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
            
        m, n = len(grid), len(grid[0])
        max_area = 0
        
        def dfs(r: int, c: int) -> int:
            # Out of bounds or water/visited cell
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == 0:
                return 0
            
            # Mark cell as visited in-place
            grid[r][c] = 0
            area = 1
            
            # Explore 4-directionally
            for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                area += dfs(r + dr, c + dc)
                
            return area

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    max_area = max(max_area, dfs(i, j))
                    
        return max_area