// ──────────────────────────────────────────────────
// Problem  : 1143. Longest Common Subsequence
// Difficulty: Medium
// Tags     : String, Dynamic Programming, Longest Common Subsequence
// Link     : https://leetcode.com/problems/longest-common-subsequence/
// Runtime  : 11 ms (beats 98%)
// Memory   : 42988000 (beats 96%)
// Language : java
// Copyright: (c) 2026 gayathri16006. All rights reserved.
// Synced by: leetie
// ──────────────────────────────────────────────────

class Solution {
    public int longestCommonSubsequence(String text1, String text2) {
        int m = text1.length();
        int n = text2.length();
        

        if (m < n) {
            return longestCommonSubsequence(text2, text1);
        }

        int[] dp = new int[n + 1];

        for (int i = 1; i <= m; i++) {
            int prev = 0; 
            char c1 = text1.charAt(i - 1);
            for (int j = 1; j <= n; j++) {
                int temp = dp[j]; 
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