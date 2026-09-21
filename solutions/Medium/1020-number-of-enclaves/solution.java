// ──────────────────────────────────────────────────
// Problem  : 1020. Number of Enclaves
// Difficulty: Medium
// Tags     : Array, Depth-First Search, Breadth-First Search, Union-Find, Matrix
// Link     : https://leetcode.com/problems/number-of-enclaves/
// Runtime  : 6 ms (beats 100%)
// Memory   : 62000000 (beats 19%)
// Language : java
// Copyright: (c) 2026 gayathri16006. All rights reserved.
// Synced by: leetie
// ──────────────────────────────────────────────────

class Solution {
    public int numEnclaves(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;

        // Traverse the first and last column
        for (int i = 0; i < m; i++) {
            if (grid[i][0] == 1) {
                dfs(grid, i, 0, m, n);
            }
            if (grid[i][n - 1] == 1) {
                dfs(grid, i, n - 1, m, n);
            }
        }

        // Traverse the first and last row
        for (int j = 0; j < n; j++) {
            if (grid[0][j] == 1) {
                dfs(grid, 0, j, m, n);
            }
            if (grid[m - 1][j] == 1) {
                dfs(grid, m - 1, j, m, n);
            }
        }

        // Count the remaining enclosed 1s
        int enclaveCount = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 1) {
                    enclaveCount++;
                }
            }
        }

        return enclaveCount;
    }

    private void dfs(int[][] grid, int r, int c, int m, int n) {
        // Out of bounds or already visited / sea cell
        if (r < 0 || r >= m || c < 0 || c >= n || grid[r][c] == 0) {
            return;
        }

       
        grid[r][c] = 0;

      
        dfs(grid, r + 1, c, m, n);
        dfs(grid, r - 1, c, m, n);
        dfs(grid, r, c + 1, m, n);
        dfs(grid, r, c - 1, m, n);
    }
}