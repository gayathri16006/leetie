# ──────────────────────────────────────────────────
# Problem  : 529. Minesweeper
# Difficulty: Medium
# Tags     : Array, Depth-First Search, Breadth-First Search, Matrix
# Link     : https://leetcode.com/problems/minesweeper/
# Runtime  : 0 ms (beats 0%)
# Memory   : 12256000 (beats 0%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        r, c = click
        m, n = len(board), len(board[0])
        
        # 1. Clicked on a mine
        if board[r][c] == 'M':
            board[r][c] = 'X'
            return board
        
        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1),  (1, 0),  (1, 1)
        ]
        
        def dfs(row, col):
            if not (0 <= row < m and 0 <= col < n) or board[row][col] != 'E':
                return
            
            # Count adjacent mines ('M' or 'X')
            mine_count = 0
            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if 0 <= nr < m and 0 <= nc < n and board[nr][nc] in ('M', 'X'):
                    mine_count += 1
            
            if mine_count > 0:
                board[row][col] = str(mine_count)
            else:
                board[row][col] = 'B'
                for dr, dc in directions:
                    dfs(row + dr, col + dc)
                    
        dfs(r, c)
        return board