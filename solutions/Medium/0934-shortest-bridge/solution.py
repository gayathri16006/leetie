# ──────────────────────────────────────────────────
# Problem  : 934. Shortest Bridge
# Difficulty: Medium
# Tags     : Array, Depth-First Search, Breadth-First Search, Matrix
# Link     : https://leetcode.com/problems/shortest-bridge/
# Runtime  : 75 ms (beats 78%)
# Memory   : 12772000 (beats 79%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

from collections import deque

class Solution(object):
    def shortestBridge(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        queue = deque()
        found = False

        # Step 1: Find one cell belonging to the first island
        for r in range(n):
            if found:
                break
            for c in range(n):
                if grid[r][c] == 1:
                    # DFS to find the entire first island, mark visited cells as 2,
                    # and enqueue them to start multi-source BFS
                    stack = [(r, c)]
                    grid[r][c] = 2
                    while stack:
                        curr_r, curr_c = stack.pop()
                        queue.append((curr_r, curr_c, 0))
                        for dr, dc in directions:
                            nr, nc = curr_r + dr, curr_c + dc
                            if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 1:
                                grid[nr][nc] = 2
                                stack.append((nr, nc))
                    found = True
                    break

        # Step 2: Multi-source BFS to reach the second island
        while queue:
            r, c, dist = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n:
                    if grid[nr][nc] == 1:
                        return dist
                    elif grid[nr][nc] == 0:
                        grid[nr][nc] = 2
                        queue.append((nr, nc, dist + 1))

        return 0