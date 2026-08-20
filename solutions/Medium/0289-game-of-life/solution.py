# ──────────────────────────────────────────────────
# Problem  : 289. Game of Life
# Difficulty: Medium
# Tags     : Array, Matrix, Simulation
# Link     : https://leetcode.com/problems/game-of-life/
# Runtime  : 0 ms (beats 0%)
# Memory   : 12492000 (beats 0%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):

  def gameOfLife(self, board):
    """Do not return anything, modify board in-place instead.

    :type board: List[List[int]]
    :rtype: None
    """
    rows, cols = len(board), len(board[0])

    # 8 directional neighbor offsets
    directions = [
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1),
    ]

    # State transitions:
    # 0 -> 0 : 0 (was dead, stays dead)
    # 1 -> 1 : 1 (was live, stays live)
    # 1 -> 0 : 2 (was live, becomes dead)
    # 0 -> 1 : 3 (was dead, becomes live)

    for r in range(rows):
      for c in range(cols):
        live_neighbors = 0

        for dr, dc in directions:
          nr, nc = r + dr, c + dc
          if 0 <= nr < rows and 0 <= nc < cols:
            # Check original state: 1 and 2 were originally live cells
            if board[nr][nc] in (1, 2):
              live_neighbors += 1

        # Apply Conway's Game of Life rules
        if board[r][c] == 1:
          if live_neighbors < 2 or live_neighbors > 3:
            board[r][c] = 2  # Live -> Dead
        else:
          if live_neighbors == 3:
            board[r][c] = 3  # Dead -> Live

    # Final pass: decode intermediate states back to 0 or 1
    for r in range(rows):
      for c in range(cols):
        if board[r][c] == 2:
          board[r][c] = 0
        elif board[r][c] == 3:
          board[r][c] = 1