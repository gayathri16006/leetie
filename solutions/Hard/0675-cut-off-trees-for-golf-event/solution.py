# ──────────────────────────────────────────────────
# Problem  : 675. Cut Off Trees for Golf Event
# Difficulty: Hard
# Tags     : Array, Breadth-First Search, Heap (Priority Queue), Matrix
# Link     : https://leetcode.com/problems/cut-off-trees-for-golf-event/
# Runtime  : 5392 ms (beats 53%)
# Memory   : 19944000 (beats 58%)
# Language : python3
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

from collections import deque
from typing import List

class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        m, n = len(forest), len(forest[0])
        
        # Collect all trees with heights > 1
        trees = []
        for r in range(m):
            for c in range(n):
                if forest[r][c] > 1:
                    trees.append((forest[r][c], r, c))
                    
        # Sort trees in ascending order of height
        trees.sort()
        
        # Standard BFS to find shortest path from (sr, sc) to (tr, tc)
        def bfs(sr: int, sc: int, tr: int, tc: int) -> int:
            if sr == tr and sc == tc:
                return 0
            
            queue = deque([(sr, sc, 0)])
            visited = {(sr, sc)}
            
            while queue:
                r, c, steps = queue.popleft()
                
                for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited:
                        if forest[nr][nc] != 0:  # 0 is an obstacle
                            if nr == tr and nc == tc:
                                return steps + 1
                            visited.add((nr, nc))
                            queue.append((nr, nc, steps + 1))
                            
            return -1

        # Start from (0, 0) and cut each tree in order
        curr_r, curr_c = 0, 0
        total_steps = 0
        
        for height, tr, tc in trees:
            steps = bfs(curr_r, curr_c, tr, tc)
            if steps == -1:
                return -1
            total_steps += steps
            curr_r, curr_c = tr, tc
            
        return total_steps