// ──────────────────────────────────────────────────
// Problem  : 1139. Largest 1-Bordered Square
// Difficulty: Medium
// Tags     : Array, Dynamic Programming, Matrix
// Link     : https://leetcode.com/problems/largest-1-bordered-square/
// Runtime  : 4 ms (beats 100%)
// Memory   : 46916000 (beats 39%)
// Language : java
// Copyright: (c) 2026 gayathri16006. All rights reserved.
// Synced by: leetie
// ──────────────────────────────────────────────────

class Solution {
    public int largest1BorderedSquare(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;

        
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

       
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                int maxPossible = Math.min(left[i][j], top[i][j]);

                for (int k = maxPossible; k > maxSide; k--) {
                    
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