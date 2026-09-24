// ──────────────────────────────────────────────────
// Problem  : 3550. Smallest Index With Digit Sum Equal to Index
// Difficulty: Easy
// Tags     : Array, Math
// Link     : https://leetcode.com/problems/smallest-index-with-digit-sum-equal-to-index/
// Runtime  : 1 ms (beats 100%)
// Memory   : 45552000 (beats 60%)
// Language : java
// Copyright: (c) 2026 gayathri16006. All rights reserved.
// Synced by: leetie
// ──────────────────────────────────────────────────

class Solution {
    public int smallestIndex(int[] nums) {
        for (int i = 0; i < nums.length; i++) {
            if (digitSum(nums[i]) == i) {
                return i;
            }
        }
        return -1;
    }

    private int digitSum(int n) {
        int sum = 0;
        while (n > 0) {
            sum += n % 10;
            n /= 10;
        }
        return sum;
    }
}