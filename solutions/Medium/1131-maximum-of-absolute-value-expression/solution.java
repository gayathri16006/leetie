// ──────────────────────────────────────────────────
// Problem  : 1131. Maximum of Absolute Value Expression
// Difficulty: Medium
// Tags     : Array, Math
// Link     : https://leetcode.com/problems/maximum-of-absolute-value-expression/
// Runtime  : 0 ms (beats 0%)
// Memory   : 42352000 (beats 0%)
// Language : java
// Copyright: (c) 2026 gayathri16006. All rights reserved.
// Synced by: leetie
// ──────────────────────────────────────────────────

class Solution {
    public int maxAbsValExpr(int[] arr1, int[] arr2) {
        int maxVal = 0;
        int n = arr1.length;
        
        // 4 sign combinations for (p, q) where p, q in {1, -1}
        int[][] signs = {{1, 1}, {1, -1}, {-1, 1}, {-1, -1}};

        for (int[] sign : signs) {
            int p = sign[0];
            int q = sign[1];

            int min = Integer.MAX_VALUE;
            int max = Integer.MIN_VALUE;

            for (int i = 0; i < n; i++) {
                int val = p * arr1[i] + q * arr2[i] + i;
                min = Math.min(min, val);
                max = Math.max(max, val);
            }

            maxVal = Math.max(maxVal, max - min);
        }

        return maxVal;
    }
}