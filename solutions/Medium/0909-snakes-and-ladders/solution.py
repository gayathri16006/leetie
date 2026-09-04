# ──────────────────────────────────────────────────
# Problem  : 909. Snakes and Ladders
# Difficulty: Medium
# Tags     : Array, Breadth-First Search, Matrix
# Link     : https://leetcode.com/problems/snakes-and-ladders/
# Runtime  : 0 ms (beats 0%)
# Memory   : 12256000 (beats 0%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

from collections import deque

class Solution(object):
    def snakesAndLadders(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        n = len(board)

        def get_coordinates(square):
            row_from_bottom = (square - 1) // n
            r = (n - 1) - row_from_bottom
            c = (square - 1) % n
            # Alternate column direction on odd rows from bottom
            if row_from_bottom % 2 == 1:
                c = (n - 1) - c
            return r, c

        target = n * n
        queue = deque([(1, 0)])  # (square, moves)
        visited = {1}

        while queue:
            curr, moves = queue.popleft()

            if curr == target:
                return moves

            for roll in range(1, 7):
                nxt = curr + roll
                if nxt > target:
                    break

                r, c = get_coordinates(nxt)
                destination = board[r][c] if board[r][c] != -1 else nxt

                if destination not in visited:
                    visited.add(destination)
                    queue.append((destination, moves + 1))

        return -1