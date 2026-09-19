// ──────────────────────────────────────────────────
// Problem  : 974. Subarray Sums Divisible by K
// Difficulty: Medium
// Tags     : Array, Hash Table, Prefix Sum
// Link     : https://leetcode.com/problems/subarray-sums-divisible-by-k/
// Runtime  : 4 ms (beats 92%)
// Memory   : 48888000 (beats 93%)
// Language : java
// Copyright: (c) 2026 gayathri16006. All rights reserved.
// Synced by: leetie
// ──────────────────────────────────────────────────

class Solution {
    public int subarraysDivByK(int[] nums, int k) {
        int[] remainderCount = new int[k];
        
        remainderCount[0] = 1;

        int prefixSum = 0;
        int count = 0;

        for (int num : nums) {
            prefixSum += num;
            
            
            int rem = (prefixSum % k + k) % k;

            
            count += remainderCount[rem];

            remainderCount[rem]++;
        }

        return count;
    }
}