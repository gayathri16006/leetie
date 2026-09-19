// ──────────────────────────────────────────────────
// Problem  : 985. Sum of Even Numbers After Queries
// Difficulty: Medium
// Tags     : Array, Simulation
// Link     : https://leetcode.com/problems/sum-of-even-numbers-after-queries/
// Runtime  : 4 ms (beats 100%)
// Memory   : 52684000 (beats 65%)
// Language : java
// Copyright: (c) 2026 gayathri16006. All rights reserved.
// Synced by: leetie
// ──────────────────────────────────────────────────

class Solution {
    public int[] sumEvenAfterQueries(int[] nums, int[][] queries) {
        int evenSum = 0;
        
        // Step 1: Calculate the initial sum of all even numbers
        for (int x : nums) {
            if (x % 2 == 0) {
                evenSum += x;
            }
        }

        int[] answer = new int[queries.length];

        // Step 2: Process each query incrementally
        for (int i = 0; i < queries.length; i++) {
            int val = queries[i][0];
            int index = queries[i][1];

            // If the current value at index is even, remove it from the running sum
            if (nums[index] % 2 == 0) {
                evenSum -= nums[index];
            }

            // Apply the query update
            nums[index] += val;

            // If the updated value is even, add it back to the running sum
            if (nums[index] % 2 == 0) {
                evenSum += nums[index];
            }

            answer[i] = evenSum;
        }

        return answer;
    }
}