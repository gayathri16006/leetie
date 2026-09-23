// ──────────────────────────────────────────────────
// Problem  : 1091. Shortest Path in Binary Matrix
// Difficulty: Medium
// Tags     : Array, Breadth-First Search, Matrix
// Link     : https://leetcode.com/problems/shortest-path-in-binary-matrix/
// Runtime  : 12 ms (beats 96%)
// Memory   : 48148000 (beats 8%)
// Language : java
// Copyright: (c) 2026 gayathri16006. All rights reserved.
// Synced by: leetie
// ──────────────────────────────────────────────────

import java.util.ArrayDeque;
import java.util.Queue;

class Solution {
    public int shortestPathBinaryMatrix(int[][] grid) {
        int n = grid.length;

        
        if (grid[0][0] != 0 || grid[n - 1][n - 1] != 0) {
            return -1;
        }

       
        if (n == 1) {
            return 1;
        }

        int[][] directions = {
            {-1, -1}, {-1, 0}, {-1, 1},
            {0, -1},           {0, 1},
            {1, -1},  {1, 0},  {1, 1}
        };

        Queue<int[]> queue = new ArrayDeque<>();
        queue.offer(new int[]{0, 0});
        grid[0][0] = 1; 

        int pathLength = 1;

        while (!queue.isEmpty()) {
            int size = queue.size();

            for (int i = 0; i < size; i++) {
                int[] curr = queue.poll();
                int r = curr[0];
                int c = curr[1];

                
                if (r == n - 1 && c == n - 1) {
                    return pathLength;
                }

               
                for (int[] dir : directions) {
                    int nr = r + dir[0];
                    int nc = c + dir[1];

                   
                    if (nr >= 0 && nr < n && nc >= 0 && nc < n && grid[nr][nc] == 0) {
                        grid[nr][nc] = 1; 
                        queue.offer(new int[]{nr, nc});
                    }
                }
            }
            pathLength++;
        }

        return -1;
    }
}