# ──────────────────────────────────────────────────
# Problem  : 778. Swim in Rising Water
# Difficulty: Hard
# Tags     : Array, Binary Search, Depth-First Search, Breadth-First Search, Union-Find, Minimax, Heap (Priority Queue), Matrix, Dijkstra's Algorithm
# Link     : https://leetcode.com/problems/swim-in-rising-water/
# Runtime  : 16 ms (beats 92%)
# Memory   : 20032000 (beats 26%)
# Language : python3
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

import heapq

class Solution:
    def swimInWater(self, grid: list[list[int]]) -> int:
        n = len(grid)
        # Min-heap stores tuples of (current_max_elevation, r, c)
        min_heap = [(grid[0][0], 0, 0)]
        visited = {(0, 0)}
        
        while min_heap:
            time, r, c = heapq.heappop(min_heap)
            
            # Reached destination bottom-right cell
            if r == n - 1 and c == n - 1:
                return time
            
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    # The time to reach the neighbor is the max of the path so far and the neighbor's elevation
                    heapq.heappush(min_heap, (max(time, grid[nr][nc]), nr, nc))
                    
        return -1