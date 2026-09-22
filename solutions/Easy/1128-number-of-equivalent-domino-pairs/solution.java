// ──────────────────────────────────────────────────
// Problem  : 1128. Number of Equivalent Domino Pairs
// Difficulty: Easy
// Tags     : Array, Hash Table, Counting
// Link     : https://leetcode.com/problems/number-of-equivalent-domino-pairs/
// Runtime  : 3 ms (beats 94%)
// Memory   : 55876000 (beats 33%)
// Language : java
// Copyright: (c) 2026 gayathri16006. All rights reserved.
// Synced by: leetie
// ──────────────────────────────────────────────────

class Solution {
    public int numEquivDominoPairs(int[][] dominoes) {
        int[] counts = new int[100];
        int pairs = 0;

        for (int[] d : dominoes) {
            
            int key = d[0] < d[1] ? d[0] * 10 + d[1] : d[1] * 10 + d[0];
            
           
            pairs += counts[key];
            
           
            counts[key]++;
        }

        return pairs;
    }
}