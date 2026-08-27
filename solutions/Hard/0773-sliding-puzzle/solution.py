# ──────────────────────────────────────────────────
# Problem  : 773. Sliding Puzzle
# Difficulty: Hard
# Tags     : Array, Dynamic Programming, Backtracking, Breadth-First Search, Memoization, Matrix, Heuristic Search, Bidirectional Search, A* Search
# Link     : https://leetcode.com/problems/sliding-puzzle/
# Runtime  : 4 ms (beats 0%)
# Memory   : 19320000 (beats 0%)
# Language : python3
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

from collections import deque

class Solution:
    def slidingPuzzle(self, board: list[list[int]]) -> int:
        target = "123450"
        start = "".join(str(val) for row in board for val in row)
        
        # Valid index transitions for each position of '0' in a 2x3 flattened grid
        neighbors = {
            0: [1, 3],
            1: [0, 2, 4],
            2: [1, 5],
            3: [0, 4],
            4: [1, 3, 5],
            5: [2, 4]
        }
        
        if start == target:
            return 0
            
        queue = deque([(start, start.index('0'), 0)])
        visited = {start}
        
        while queue:
            state, zero_idx, moves = queue.popleft()
            
            if state == target:
                return moves
            
            state_list = list(state)
            for next_idx in neighbors[zero_idx]:
                # Swap '0' with adjacent tile
                state_list[zero_idx], state_list[next_idx] = state_list[next_idx], state_list[zero_idx]
                next_state = "".join(state_list)
                
                if next_state not in visited:
                    visited.add(next_state)
                    queue.append((next_state, next_idx, moves + 1))
                    
                # Backtrack swap
                state_list[zero_idx], state_list[next_idx] = state_list[next_idx], state_list[zero_idx]
                
        return -1