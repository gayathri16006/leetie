# ──────────────────────────────────────────────────
# Problem  : 417. Pacific Atlantic Water Flow
# Difficulty: Medium
# Tags     : Array, Depth-First Search, Breadth-First Search, Matrix
# Link     : https://leetcode.com/problems/pacific-atlantic-water-flow/
# Runtime  : 52 ms (beats 35%)
# Memory   : 14060000 (beats 17%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):

    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        if not heights or not heights[0]:
            return []

        rows, cols = len(heights), len(heights[0])
        pac = set()
        atl = set()

        def dfs(r, c, visit, prev_height):
            if (
                r < 0
                or c < 0
                or r >= rows
                or c >= cols
                or (r, c) in visit
                or heights[r][c] < prev_height
            ):
                return

            visit.add((r, c))

            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                dfs(r + dr, c + dc, visit, heights[r][c])

        # Traverse along borders: top & bottom rows
        for c in range(cols):
            dfs(0, c, pac, heights[0][c])  # Top row (Pacific)
            dfs(rows - 1, c, atl, heights[rows - 1][c])  # Bottom row (Atlantic)

        # Traverse along borders: left & right columns
        for r in range(rows):
            dfs(r, 0, pac, heights[r][0])  # Left column (Pacific)
            dfs(r, cols - 1, atl, heights[r][cols - 1])  # Right column (Atlantic)

        # Cells reachable from both oceans
        return [[r, c] for r, c in (pac & atl)]