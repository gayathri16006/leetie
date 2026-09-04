# ──────────────────────────────────────────────────
# Problem  : 827. Making A Large Island
# Difficulty: Hard
# Tags     : Array, Depth-First Search, Breadth-First Search, Union-Find, Matrix
# Link     : https://leetcode.com/problems/making-a-large-island/
# Runtime  : 3 ms (beats 0%)
# Memory   : 12308000 (beats 0%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def largestIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        island_sizes = {}
        island_id = 2

        def dfs(r, c, tag):
            stack = [(r, c)]
            grid[r][c] = tag
            size = 0
            while stack:
                cr, cc = stack.pop()
                size += 1
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nr, nc = cr + dr, cc + dc
                    if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 1:
                        grid[nr][nc] = tag
                        stack.append((nr, nc))
            return size

        # Phase 1: Label each island and store its size
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    island_sizes[island_id] = dfs(r, c, island_id)
                    island_id += 1

        # If the grid is already all 1s or has no islands
        if not island_sizes:
            return 1
        max_size = max(island_sizes.values())

        # Phase 2: Try turning each 0 into 1
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 0:
                    seen = set()
                    cur_size = 1
                    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] > 1:
                            tag = grid[nr][nc]
                            if tag not in seen:
                                seen.add(tag)
                                cur_size += island_sizes[tag]
                    max_size = max(max_size, cur_size)

        return min(max_size, n * n)