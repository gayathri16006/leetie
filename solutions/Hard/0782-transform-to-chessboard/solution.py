# ──────────────────────────────────────────────────
# Problem  : 782. Transform to Chessboard
# Difficulty: Hard
# Tags     : Array, Math, Bit Manipulation, Matrix
# Link     : https://leetcode.com/problems/transform-to-chessboard/
# Runtime  : 3 ms (beats 60%)
# Memory   : 19364000 (beats 62%)
# Language : python3
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def movesToChessboard(self, board: list[list[int]]) -> int:
        n = len(board)
        
        # 1. Validate that all rows/columns are either identical to the 1st or its exact inverse
        for r in range(n):
            for c in range(n):
                if (board[0][0] ^ board[r][0] ^ board[0][c] ^ board[r][c]) != 0:
                    return -1
        
        row_sum = sum(board[0])
        col_sum = sum(board[r][0] for r in range(n))
        
        # 2. Check that count of 0s and 1s differs by at most 1
        if not (n // 2 <= row_sum <= (n + 1) // 2):
            return -1
        if not (n // 2 <= col_sum <= (n + 1) // 2):
            return -1
        
        # 3. Count mismatches against the alternating pattern starting with 0 (0, 1, 0, 1...)
        row_diff = sum(board[0][c] != (c % 2) for c in range(n))
        col_diff = sum(board[r][0] != (r % 2) for r in range(n))
        
        # Calculate minimum swaps for rows and columns
        if n % 2 == 1:
            # If N is odd, the start pattern is fixed by which count (0 or 1) has majority
            if row_diff % 2 != 0:
                row_diff = n - row_diff
            if col_diff % 2 != 0:
                col_diff = n - col_diff
        else:
            # If N is even, choose the minimum mismatch between starting with 0 or 1
            row_diff = min(row_diff, n - row_diff)
            col_diff = min(col_diff, n - col_diff)
            
        # Each swap fixes 2 misplaced lines
        return (row_diff + col_diff) // 2