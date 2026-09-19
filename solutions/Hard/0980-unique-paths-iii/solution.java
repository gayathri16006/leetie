// ──────────────────────────────────────────────────
// Problem  : 980. Unique Paths III
// Difficulty: Hard
// Tags     : Array, Backtracking, Bit Manipulation, Matrix, Hamiltonian Path
// Link     : https://leetcode.com/problems/unique-paths-iii/
// Runtime  : 0 ms (beats 0%)
// Memory   : 42396000 (beats 0%)
// Language : java
// Copyright: (c) 2026 gayathri16006. All rights reserved.
// Synced by: leetie
// ──────────────────────────────────────────────────

class Solution {
    private int paths = 0;
    private int nonObstacleCount = 1; // Start with 1 to count the starting square

    public int uniquePathsIII(int[][] grid) {
        paths = 0;
        nonObstacleCount = 1;
        
        int startR = 0;
        int startC = 0;
        int m = grid.length;
        int n = grid[0].length;

        // Find the start square and count all visitable cells
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 0) {
                    nonObstacleCount++;
                } else if (grid[i][j] == 1) {
                    startR = i;
                    startC = j;
                }
            }
        }

        backtrack(grid, startR, startC, 0);
        return paths;
    }

    private void backtrack(int[][] grid, int r, int c, int visited) {
        // Boundary and obstacle / visited check
        if (r < 0 || r >= grid.length || c < 0 || c >= grid[0].length || grid[r][c] == -1) {
            return;
        }

        // Reached destination square
        if (grid[r][c] == 2) {
            if (visited == nonObstacleCount) {
                paths++;
            }
            return;
        }

        // Mark current square as visited
        int temp = grid[r][c];
        grid[r][c] = -1;

        // Explore all 4 directions
        backtrack(grid, r + 1, c, visited + 1);
        backtrack(grid, r - 1, c, visited + 1);
        backtrack(grid, r, c + 1, visited + 1);
        backtrack(grid, r, c - 1, visited + 1);

        // Backtrack: restore original cell state
        grid[r][c] = temp;
    }
}