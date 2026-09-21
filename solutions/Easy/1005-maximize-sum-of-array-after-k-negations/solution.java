// ──────────────────────────────────────────────────
// Problem  : 1005. Maximize Sum Of Array After K Negations
// Difficulty: Easy
// Tags     : Array, Greedy, Sorting
// Link     : https://leetcode.com/problems/maximize-sum-of-array-after-k-negations/
// Runtime  : 6 ms (beats 89%)
// Memory   : 44556000 (beats 57%)
// Language : java
// Copyright: (c) 2026 gayathri16006. All rights reserved.
// Synced by: leetie
// ──────────────────────────────────────────────────

class Solution {
    public int largestSumAfterKNegations(int[] nums, int k) {
        java.util.Arrays.sort(nums);
        
        int sum = 0;
        int minVal = Integer.MAX_VALUE;

        for (int i = 0; i < nums.length; i++) {// Flip negative numbers while k > 0
            if (nums[i] < 0 && k > 0) {
                nums[i] = -nums[i];
                k--;
            }
            sum += nums[i];
            minVal = Math.min(minVal, nums[i]);
        }

       
        if (k % 2 != 0) {
            sum -= 2 * minVal;
        }

        return sum;
    }
}