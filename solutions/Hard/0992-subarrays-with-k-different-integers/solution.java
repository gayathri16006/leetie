// ──────────────────────────────────────────────────
// Problem  : 992. Subarrays with K Different Integers
// Difficulty: Hard
// Tags     : Array, Hash Table, Sliding Window, Counting
// Link     : https://leetcode.com/problems/subarrays-with-k-different-integers/
// Runtime  : 0 ms (beats 0%)
// Memory   : 42444000 (beats 0%)
// Language : java
// Copyright: (c) 2026 gayathri16006. All rights reserved.
// Synced by: leetie
// ──────────────────────────────────────────────────

class Solution {
    public int subarraysWithKDistinct(int[] nums, int k) {
        return atMostK(nums, k) - atMostK(nums, k - 1);
    }

    private int atMostK(int[] nums, int k) {
        if (k == 0) return 0;

        int[] count = new int[nums.length + 1];
        int left = 0;
        int distinct = 0;
        int totalSubarrays = 0;

        for (int right = 0; right < nums.length; right++) {
            if (count[nums[right]] == 0) {
                distinct++;
            }
            count[nums[right]]++;

            while (distinct > k) {
                count[nums[left]]--;
                if (count[nums[left]] == 0) {
                    distinct--;
                }
                left++;
            }

            // Number of valid subarrays ending at 'right'
            totalSubarrays += (right - left + 1);
        }

        return totalSubarrays;
    }
}