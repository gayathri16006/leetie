# ──────────────────────────────────────────────────
# Problem  : 566. Reshape the Matrix
# Difficulty: Easy
# Tags     : Array, Matrix, Simulation
# Link     : https://leetcode.com/problems/reshape-the-matrix/
# Runtime  : 0 ms (beats 0%)
# Memory   : 12528000 (beats 0%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def matrixReshape(self, mat, r, c):
        m, n = len(mat), len(mat[0])
        
        # Check if reshaping is possible
        if m * n != r * c:
            return mat
        
        # Create the new r x c matrix
        res = [[0] * c for _ in range(r)]
        
        for i in range(m * n):
            # Map 1D index i to (original_row, original_col) and (new_row, new_col)
            res[i // c][i % c] = mat[i // n][i % n]
            
        return res