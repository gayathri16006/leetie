// ──────────────────────────────────────────────────
// Problem  : 1658. Minimum Operations to Reduce X to Zero
// Difficulty: Medium
// Tags     : Array, Hash Table, Binary Search, Sliding Window, Prefix Sum
// Link     : https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/
// Runtime  : 4 ms (beats 98%)
// Memory   : 101956000 (beats 76%)
// Language : java
// Copyright: (c) 2026 gayathri16006. All rights reserved.
// Synced by: leetie
// ──────────────────────────────────────────────────

class Solution {
    public int minOperations(int[] nums, int x) {
        int totalSum = 0;
        for (int num : nums) {
            totalSum += num;
        }

        int target = totalSum - x;

        // If target is negative, sum of elements is less than x
        if (target < 0) return -1;
        // If target is 0, we need to remove all elements
        if (target == 0) return nums.length;

        int left = 0;
        int currentSum = 0;
        int maxLen = -1;

        for (int right = 0; right < nums.length; right++) {
            currentSum += nums[right];

            // Shrink the window from the left while currentSum > target
            while (currentSum > target && left <= right) {
                currentSum -= nums[left++];
            }

           
            if (currentSum == target) {
                maxLen = Math.max(maxLen, right - left + 1);
            }
        }

        return maxLen == -1 ? -1 : nums.length - maxLen;
    }
}