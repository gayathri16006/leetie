// ──────────────────────────────────────────────────
// Problem  : 1015. Smallest Integer Divisible by K
// Difficulty: Medium
// Tags     : Hash Table, Math, Pigeonhole Principle
// Link     : https://leetcode.com/problems/smallest-integer-divisible-by-k/
// Runtime  : 2 ms (beats 99%)
// Memory   : 42184000 (beats 45%)
// Language : java
// Copyright: (c) 2026 gayathri16006. All rights reserved.
// Synced by: leetie
// ──────────────────────────────────────────────────

class Solution {
    public int smallestRepunitDivByK(int k) {
        // If k is divisible by 2 or 5, no number consisting only of 1s can be divisible by k
        if (k % 2 == 0 || k % 5 == 0) {
            return -1;
        }

        int remainder = 0;
        for (int length = 1; length <= k; length++) {
            remainder = (remainder * 10 + 1) % k;
            if (remainder == 0) {
                return length;
            }
        }

        return -1;
    }
}