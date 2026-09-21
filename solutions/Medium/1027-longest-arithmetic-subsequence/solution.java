// ──────────────────────────────────────────────────
// Problem  : 1027. Longest Arithmetic Subsequence
// Difficulty: Medium
// Tags     : Array, Hash Table, Binary Search, Dynamic Programming
// Link     : https://leetcode.com/problems/longest-arithmetic-subsequence/
// Runtime  : 0 ms (beats 0%)
// Memory   : 42720000 (beats 0%)
// Language : java
// Copyright: (c) 2026 gayathri16006. All rights reserved.
// Synced by: leetie
// ──────────────────────────────────────────────────

class Solution {
    public int longestArithSeqLength(int[] nums) {
        int n = nums.length;
        if (n <= 2) return n;

        // dp[i][diff] stores the length of arithmetic subsequence ending at i with common difference diff
        // Difference range: -500 to 500, mapped to 0 to 1000 using an offset of 500
        int[][] dp = new int[n][1001];
        int maxLen = 2;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < i; j++) {
                int diff = nums[i] - nums[j] + 500; // Apply offset
                
                // If there's an existing sequence ending at j with this diff, extend it.
                // Otherwise, the pair (nums[j], nums[i]) forms a sequence of length 2.
                dp[i][diff] = Math.max(dp[i][diff], dp[j][diff] > 0 ? dp[j][diff] + 1 : 2);
                
                maxLen = Math.max(maxLen, dp[i][diff]);
            }
        }

        return maxLen;
    }
}