# ──────────────────────────────────────────────────
# Problem  : 576. Out of Boundary Paths
# Difficulty: Medium
# Tags     : Dynamic Programming
# Link     : https://leetcode.com/problems/out-of-boundary-paths/
# Runtime  : 65 ms (beats 50%)
# Memory   : 18764000 (beats 42%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def findPaths(self, m, n, maxMove, startRow, startColumn):
        """
        :type m: int
        :type n: int
        :type maxMove: int
        :type startRow: int
        :type startColumn: int
        :rtype: int
        """
        MOD = 10**9 + 7
        memo = {}

        def dfs(r, c, moves_left):
            # Out of bounds: 1 valid path found
            if r < 0 or r >= m or c < 0 or c >= n:
                return 1
            # No moves remaining and still inside grid: 0 paths
            if moves_left == 0:
                return 0

            state = (r, c, moves_left)
            if state in memo:
                return memo[state]

            paths = (
                dfs(r + 1, c, moves_left - 1) +
                dfs(r - 1, c, moves_left - 1) +
                dfs(r, c + 1, moves_left - 1) +
                dfs(r, c - 1, moves_left - 1)
            ) % MOD

            memo[state] = paths
            return paths

        return dfs(startRow, startColumn, maxMove)