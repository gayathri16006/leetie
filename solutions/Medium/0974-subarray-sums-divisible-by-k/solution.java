// ──────────────────────────────────────────────────
// Problem  : 974. Subarray Sums Divisible by K
// Difficulty: Medium
// Tags     : Array, Hash Table, Prefix Sum
// Link     : https://leetcode.com/problems/subarray-sums-divisible-by-k/
// Runtime  : 0 ms (beats 0%)
// Memory   : 42272000 (beats 0%)
// Language : java
// Copyright: (c) 2026 gayathri16006. All rights reserved.
// Synced by: leetie
// ──────────────────────────────────────────────────

class Solution {
    public int subarraysDivByK(int[] nums, int k) {
        int[] remainderCount = new int[k];
        // Base case: a prefix sum of 0 has occurred once
        remainderCount[0] = 1;

        int prefixSum = 0;
        int count = 0;

        for (int num : nums) {
            prefixSum += num;
            
            // Normalize remainder to ensure it's in the range [0, k - 1]
            int rem = (prefixSum % k + k) % k;

            // If this remainder has been seen before, each prior occurrence forms a valid subarray
            count += remainderCount[rem];

            remainderCount[rem]++;
        }

        return count;
    }
}