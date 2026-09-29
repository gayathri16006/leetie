// ──────────────────────────────────────────────────
// Problem  : 2267.  Check if There Is a Valid Parentheses String Path
// Difficulty: Hard
// Tags     : Array, Dynamic Programming, Matrix, Bracket Sequences
// Link     : https://leetcode.com/problems/check-if-there-is-a-valid-parentheses-string-path/
// Runtime  : 4 ms (beats 97%)
// Memory   : 75116000 (beats 67%)
// Language : java
// Copyright: (c) 2026 gayathri16006. All rights reserved.
// Synced by: leetie
// ──────────────────────────────────────────────────

class Solution {
    private Boolean[][][] memo;
    private int m, n;

    public boolean hasValidPath(char[][] grid) {
        m = grid.length;
        n = grid[0].length;

        // An odd total length can never be balanced
        if ((m + n - 1) % 2 != 0) return false;
        // Must start with '(' and end with ')'
        if (grid[0][0] == ')' || grid[m - 1][n - 1] == '(') return false;

        // Maximum open brackets needed is (m + n - 1) / 2 + 1
        int maxOpen = (m + n) / 2;
        memo = new Boolean[m][n][maxOpen + 1];

        return dfs(grid, 0, 0, 0);
    }

    private boolean dfs(char[][] grid, int r, int c, int open) {
        open += (grid[r][c] == '(' ? 1 : -1);

        // Invalid prefix balance
        if (open < 0) return false;

        // Open brackets cannot exceed half of total path length
        int maxOpen = (m + n) / 2;
        if (open > maxOpen) return false;

        // Pruning: remaining steps must be at least equal to open count to balance out
        int remainingSteps = (m - 1 - r) + (n - 1 - c);
        if (open > remainingSteps) return false;

        // Reached destination
        if (r == m - 1 && c == n - 1) {
            return open == 0;
        }

        if (memo[r][c][open] != null) {
            return memo[r][c][open];
        }

        boolean found = false;
     
        if (r + 1 < m) {
            found = dfs(grid, r + 1, c, open);
        }
        
        if (!found && c + 1 < n) {
            found = dfs(grid, r, c + 1, open);
        }

        return memo[r][c][open] = found;
    }
}