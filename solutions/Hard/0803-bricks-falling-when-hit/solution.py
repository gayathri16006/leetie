# ──────────────────────────────────────────────────
# Problem  : 803. Bricks Falling When Hit
# Difficulty: Hard
# Tags     : Array, Union-Find, Matrix
# Link     : https://leetcode.com/problems/bricks-falling-when-hit/
# Runtime  : 0 ms (beats 0%)
# Memory   : 19408000 (beats 0%)
# Language : python3
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, i: int) -> int:
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i: int, j: int):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            self.parent[root_i] = root_j
            self.size[root_j] += self.size[root_i]

    def get_size(self, i: int) -> int:
        return self.size[self.find(i)]


class Solution:
    def hitBricks(self, grid: list[list[int]], hits: list[list[int]]) -> list[int]:
        m, n = len(grid), len(grid[0])
        roof_node = m * n  # Virtual node representing connection to the top roof

        # Step 1: Copy grid and simulate removing all hit bricks
        copy_grid = [row[:] for row in grid]
        for r, c in hits:
            copy_grid[r][c] = 0

        # Step 2: Initialize Union-Find on remaining bricks
        uf = UnionFind(m * n + 1)

        def node_id(r: int, c: int) -> int:
            return r * n + c

        for r in range(m):
            for c in range(n):
                if copy_grid[r][c] == 1:
                    idx = node_id(r, c)
                    if r == 0:
                        uf.union(idx, roof_node)
                    if r > 0 and copy_grid[r - 1][c] == 1:
                        uf.union(idx, node_id(r - 1, c))
                    if c > 0 and copy_grid[r][c - 1] == 1:
                        uf.union(idx, node_id(r, c - 1))

        # Step 3: Process hits in reverse order (adding bricks back)
        res = [0] * len(hits)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for k in range(len(hits) - 1, -1, -1):
            r, c = hits[k]
            # If no brick was originally here, nothing falls
            if grid[r][c] == 0:
                continue

            prev_roof_size = uf.get_size(roof_node)
            curr_node = node_id(r, c)

            # Connect with the roof if on top row
            if r == 0:
                uf.union(curr_node, roof_node)

            # Connect with valid adjacent bricks
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and copy_grid[nr][nc] == 1:
                    uf.union(curr_node, node_id(nr, nc))

            copy_grid[r][c] = 1
            new_roof_size = uf.get_size(roof_node)

            # Fallen bricks = (increase in roof size) - 1 (the hit brick itself)
            res[k] = max(0, new_roof_size - prev_roof_size - 1)

        return res