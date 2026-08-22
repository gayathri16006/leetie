# ──────────────────────────────────────────────────
# Problem  : 498. Diagonal Traverse
# Difficulty: Medium
# Tags     : Array, Matrix, Simulation
# Link     : https://leetcode.com/problems/diagonal-traverse/
# Runtime  : 9 ms (beats 76%)
# Memory   : 14556000 (beats 84%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def findDiagonalOrder(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        if not mat or not mat[0]:
            return []

        m, n = len(mat), len(mat[0])
        r, c = 0, 0
        direction = 1  # 1 for up-right, -1 for down-left
        result = []

        for _ in range(m * n):
            result.append(mat[r][c])

            if direction == 1:
                # Moving up-right: next candidate is (r - 1, c + 1)
                if c == n - 1:  # Hits right boundary: move down, switch direction
                    r += 1
                    direction = -1
                elif r == 0:    # Hits top boundary: move right, switch direction
                    c += 1
                    direction = -1
                else:
                    r -= 1
                    c += 1
            else:
                # Moving down-left: next candidate is (r + 1, c - 1)
                if r == m - 1:  # Hits bottom boundary: move right, switch direction
                    c += 1
                    direction = 1
                elif c == 0:    # Hits left boundary: move down, switch direction
                    r += 1
                    direction = 1
                else:
                    r += 1
                    c -= 1

        return result