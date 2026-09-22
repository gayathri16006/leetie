// ──────────────────────────────────────────────────
// Problem  : 1129. Shortest Path with Alternating Colors
// Difficulty: Medium
// Tags     : Breadth-First Search, Graph Theory
// Link     : https://leetcode.com/problems/shortest-path-with-alternating-colors/
// Runtime  : 5 ms (beats 74%)
// Memory   : 46560000 (beats 71%)
// Language : java
// Copyright: (c) 2026 gayathri16006. All rights reserved.
// Synced by: leetie
// ──────────────────────────────────────────────────

import java.util.*;

class Solution {
    public int[] shortestAlternatingPaths(int n, int[][] redEdges, int[][] blueEdges) {
       
        List<Integer>[][] graph = new ArrayList[2][n];
        for (int i = 0; i < 2; i++) {
            for (int j = 0; j < n; j++) {
                graph[i][j] = new ArrayList<>();
            }
        }
        
        for (int[] edge : redEdges) {
            graph[0][edge[0]].add(edge[1]);
        }
        for (int[] edge : blueEdges) {
            graph[1][edge[0]].add(edge[1]);
        }

        int[] answer = new int[n];
        Arrays.fill(answer, -1);

       
        boolean[][] visited = new boolean[n][2];

        
        Queue<int[]> queue = new LinkedList<>();

        
        queue.offer(new int[]{0, 0, 0});
        queue.offer(new int[]{0, 1, 0});
        visited[0][0] = true;
        visited[0][1] = true;

        while (!queue.isEmpty()) {
            int[] curr = queue.poll();
            int u = curr[0];
            int color = curr[1];
            int dist = curr[2];

            if (answer[u] == -1) {
                answer[u] = dist;
            }

            int nextColor = 1 - color; 
            for (int v : graph[nextColor][u]) {
                if (!visited[v][nextColor]) {
                    visited[v][nextColor] = true;
                    queue.offer(new int[]{v, nextColor, dist + 1});
                }
            }
        }

        return answer;
    }
}