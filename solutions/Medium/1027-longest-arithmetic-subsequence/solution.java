// ──────────────────────────────────────────────────
// Problem  : 1027. Longest Arithmetic Subsequence
// Difficulty: Medium
// Tags     : Array, Hash Table, Binary Search, Dynamic Programming
// Link     : https://leetcode.com/problems/longest-arithmetic-subsequence/
// Runtime  : 40 ms (beats 85%)
// Memory   : 69180000 (beats 68%)
// Language : java
// Copyright: (c) 2026 gayathri16006. All rights reserved.
// Synced by: leetie
// ──────────────────────────────────────────────────

class Solution {
    public int longestArithSeqLength(int[] nums) {
        int n = nums.length;
        if (n <= 2) return n;

        
        int[][] dp = new int[n][1001];
        int maxLen = 2;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < i; j++) {
                int diff = nums[i] - nums[j] + 500; 
                
               
                dp[i][diff] = Math.max(dp[i][diff], dp[j][diff] > 0 ? dp[j][diff] + 1 : 2);
                
                maxLen = Math.max(maxLen, dp[i][diff]);
            }
        }

        return maxLen;
    }
}