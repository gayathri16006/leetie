# ──────────────────────────────────────────────────
# Problem  : 867. Transpose Matrix
# Difficulty: Easy
# Tags     : Array, Matrix, Simulation
# Link     : https://leetcode.com/problems/transpose-matrix/
# Runtime  : 0 ms (beats 100%)
# Memory   : 12860000 (beats 78%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n = len(matrix), len(matrix[0])
        
        # Initialize an n x m matrix
        ans = [[0] * m for _ in range(n)]
        
        for r in range(m):
            for c in range(n):
                ans[c][r] = matrix[r][c]
                
        return ans