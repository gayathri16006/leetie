// ──────────────────────────────────────────────────
// Problem  : 1143. Longest Common Subsequence
// Difficulty: Medium
// Tags     : String, Dynamic Programming, Longest Common Subsequence
// Link     : https://leetcode.com/problems/longest-common-subsequence/
// Runtime  : 0 ms (beats 0%)
// Memory   : 43148000 (beats 0%)
// Language : java
// Copyright: (c) 2026 gayathri16006. All rights reserved.
// Synced by: leetie
// ──────────────────────────────────────────────────

class Solution {
    public int longestCommonSubsequence(String text1, String text2) {
        int m = text1.length();
        int n = text2.length();

        // Ensure text2 is the shorter string to optimize space to O(min(m, n))
        if (m < n) {
            return longestCommonSubsequence(text2, text1);
        }

        int[] dp = new int[n + 1];

        for (int i = 1; i <= m; i++) {
            int prev = 0; // Represents dp[i-1][j-1]
            char c1 = text1.charAt(i - 1);
            for (int j = 1; j <= n; j++) {
                int temp = dp[j]; // Store current dp[j] (which is dp[i-1][j] for next column)
                if (c1 == text2.charAt(j - 1)) {
                    dp[j] = prev + 1;
                } else {
                    dp[j] = Math.max(dp[j], dp[j - 1]);
                }
                prev = temp;
            }
        }

        return dp[n];
    }
}