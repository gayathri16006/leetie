// ──────────────────────────────────────────────────
// Problem  : 1139. Largest 1-Bordered Square
// Difficulty: Medium
// Tags     : Array, Dynamic Programming, Matrix
// Link     : https://leetcode.com/problems/largest-1-bordered-square/
// Runtime  : 0 ms (beats 0%)
// Memory   : 42552000 (beats 0%)
// Language : java
// Copyright: (c) 2026 gayathri16006. All rights reserved.
// Synced by: leetie
// ──────────────────────────────────────────────────

class Solution {
    public int largest1BorderedSquare(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;

        // left[i][j]: consecutive 1s ending at (i, j) horizontally
        // top[i][j]:  consecutive 1s ending at (i, j) vertically
        int[][] left = new int[m][n];
        int[][] top = new int[m][n];

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 1) {
                    left[i][j] = (j > 0 ? left[i][j - 1] : 0) + 1;
                    top[i][j] = (i > 0 ? top[i - 1][j] : 0) + 1;
                }
            }
        }

        int maxSide = 0;

        // Consider each cell (i, j) as the bottom-right corner of the square
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                int maxPossible = Math.min(left[i][j], top[i][j]);

                for (int k = maxPossible; k > maxSide; k--) {
                    // Check if top edge and left edge also have length >= k
                    if (left[i - k + 1][j] >= k && top[i][j - k + 1] >= k) {
                        maxSide = k;
                        break;
                    }
                }
            }
        }

        return maxSide * maxSide;
    }
}