// ──────────────────────────────────────────────────
// Problem  : 1000. Minimum Cost to Merge Stones
// Difficulty: Hard
// Tags     : Array, Dynamic Programming, Prefix Sum
// Link     : https://leetcode.com/problems/minimum-cost-to-merge-stones/
// Runtime  : 0 ms (beats 0%)
// Memory   : 42432000 (beats 0%)
// Language : java
// Copyright: (c) 2026 gayathri16006. All rights reserved.
// Synced by: leetie
// ──────────────────────────────────────────────────

class Solution {
    public int mergeStones(int[] stones, int k) {
        int n = stones.length;
        
        // If it's impossible to merge into 1 pile
        if ((n - 1) % (k - 1) != 0) {
            return -1;
        }

        // Prefix sums to quickly calculate range sums in O(1)
        int[] prefixSum = new int[n + 1];
        for (int i = 0; i < n; i++) {
            prefixSum[i + 1] = prefixSum[i] + stones[i];
        }

        // dp[i][j] is the minimum cost to merge subarray stones[i..j]
        // into the fewest possible piles
        int[][] dp = new int[n][n];

        // Length of the sub-interval
        for (int len = k; len <= n; len++) {
            for (int i = 0; i + len - 1 < n; i++) {
                int j = i + len - 1;
                dp[i][j] = Integer.MAX_VALUE;

                // Split at m, advancing by (k - 1) steps
                for (int m = i; m < j; m += k - 1) {
                    dp[i][j] = Math.min(dp[i][j], dp[i][m] + dp[m + 1][j]);
                }

               
                if ((j - i) % (k - 1) == 0) {
                    dp[i][j] += prefixSum[j + 1] - prefixSum[i];
                }
            }
        }

        return dp[0][n - 1];
    }
}