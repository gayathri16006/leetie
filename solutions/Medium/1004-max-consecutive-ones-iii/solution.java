// ──────────────────────────────────────────────────
// Problem  : 1004. Max Consecutive Ones III
// Difficulty: Medium
// Tags     : Array, Binary Search, Sliding Window, Prefix Sum
// Link     : https://leetcode.com/problems/max-consecutive-ones-iii/
// Runtime  : 0 ms (beats 0%)
// Memory   : 42516000 (beats 0%)
// Language : java
// Copyright: (c) 2026 gayathri16006. All rights reserved.
// Synced by: leetie
// ──────────────────────────────────────────────────

class Solution {
    public int longestOnes(int[] nums, int k) {
        int left = 0;
        int zeroCount = 0;
        int maxLength = 0;

        for (int right = 0; right < nums.length; right++) {
            if (nums[right] == 0) {
                zeroCount++;
            }

            while (zeroCount > k) {
                if (nums[left] == 0) {
                    zeroCount--;
                }
                left++;
            }

            maxLength = Math.max(maxLength, right - left + 1);
        }

        return maxLength;
    }
}