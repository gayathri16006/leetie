// ──────────────────────────────────────────────────
// Problem  : 982. Triples with Bitwise AND Equal To Zero
// Difficulty: Hard
// Tags     : Array, Hash Table, Bit Manipulation
// Link     : https://leetcode.com/problems/triples-with-bitwise-and-equal-to-zero/
// Runtime  : 72 ms (beats 92%)
// Memory   : 46716000 (beats 52%)
// Language : java
// Copyright: (c) 2026 gayathri16006. All rights reserved.
// Synced by: leetie
// ──────────────────────────────────────────────────

class Solution {
    public int countTriplets(int[] nums) {
        // nums[i] < 2^16, so any bitwise AND result will be in the range [0, 65535]
        int[] count = new int[1 << 16];

        // Step 1: Precompute frequencies of (nums[i] & nums[j])
        for (int a : nums) {
            for (int b : nums) {
                count[a & b]++;
            }
        }

        int total = 0;

        // Step 2: Check each precomputed pair result against every nums[k]
        for (int ab = 0; ab < (1 << 16); ab++) {
            if (count[ab] == 0) continue;

            for (int c : nums) {
                if ((ab & c) == 0) {
                    total += count[ab];
                }
            }
        }

        return total;
    }
}