# ──────────────────────────────────────────────────
# Problem  : 766. Toeplitz Matrix
# Difficulty: Easy
# Tags     : Array, Matrix
# Link     : https://leetcode.com/problems/toeplitz-matrix/
# Runtime  : 0 ms (beats 0%)
# Memory   : 19184000 (beats 0%)
# Language : python3
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def isToeplitzMatrix(self, matrix: list[list[int]]) -> bool:
        m, n = len(matrix), len(matrix[0])
        
        # Check if every element matches its top-left diagonal neighbor
        for r in range(1, m):
            for c in range(1, n):
                if matrix[r][c] != matrix[r - 1][c - 1]:
                    return False
                    
        return True