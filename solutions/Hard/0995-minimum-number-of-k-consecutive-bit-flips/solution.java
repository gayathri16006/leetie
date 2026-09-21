// ──────────────────────────────────────────────────
// Problem  : 995. Minimum Number of K Consecutive Bit Flips
// Difficulty: Hard
// Tags     : Array, Bit Manipulation, Queue, Sliding Window, Prefix Sum, Brute-Force Search
// Link     : https://leetcode.com/problems/minimum-number-of-k-consecutive-bit-flips/
// Runtime  : 5 ms (beats 69%)
// Memory   : 75036000 (beats 29%)
// Language : java
// Copyright: (c) 2026 gayathri16006. All rights reserved.
// Synced by: leetie
// ──────────────────────────────────────────────────

class Solution {
    public int minKBitFlips(int[] nums, int k) {
        int n = nums.length;
        int ans = 0;
        int currentFlips = 0; // Number of active flips covering index i

        for (int i = 0; i < n; i++) {
            // Remove the effect of the flip that started at i - k
            if (i >= k && nums[i - k] > 1) {
                currentFlips--;
            }

            // If current bit is 0 after considering flips:
            // (nums[i] + currentFlips) % 2 == 0 means it effectively is 0
            if ((nums[i] + currentFlips) % 2 == 0) {
               
                if (i + k > n) {
                    return -1;
                }
               
                nums[i] += 2;
                currentFlips++;
                ans++;
            }
        }

        return ans;
    }
}