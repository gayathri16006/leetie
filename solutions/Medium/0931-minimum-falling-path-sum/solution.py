# ──────────────────────────────────────────────────
# Problem  : 931. Minimum Falling Path Sum
# Difficulty: Medium
# Tags     : Array, Dynamic Programming, Matrix
# Link     : https://leetcode.com/problems/minimum-falling-path-sum/
# Runtime  : 25 ms (beats 62%)
# Memory   : 12912000 (beats 84%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def minFallingPathSum(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        n = len(matrix)
        
        # Traverse from the second-to-last row up to the first row
        for r in range(n - 2, -1, -1):
            for c in range(n):
                # Below element
                down = matrix[r + 1][c]
                # Diagonally left element (if within bounds)
                down_left = matrix[r + 1][c - 1] if c > 0 else float('inf')
                # Diagonally right element (if within bounds)
                down_right = matrix[r + 1][c + 1] if c < n - 1 else float('inf')
                
                matrix[r][c] += min(down, down_left, down_right)
                
        # The answer is the minimum value in the top row
        return min(matrix[0])