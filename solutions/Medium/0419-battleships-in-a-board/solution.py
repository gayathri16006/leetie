# ──────────────────────────────────────────────────
# Problem  : 419. Battleships in a Board
# Difficulty: Medium
# Tags     : Array, Depth-First Search, Matrix
# Link     : https://leetcode.com/problems/battleships-in-a-board/
# Runtime  : 0 ms (beats 100%)
# Memory   : 14272000 (beats 31%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):

    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        if not board or not board[0]:
            return 0

        rows, cols = len(board), len(board[0])
        count = 0

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "X":
                    # Check if this cell is the top-left head of a battleship
                    if r > 0 and board[r - 1][c] == "X":
                        continue
                    if c > 0 and board[r][c - 1] == "X":
                        continue
                    count += 1

        return count