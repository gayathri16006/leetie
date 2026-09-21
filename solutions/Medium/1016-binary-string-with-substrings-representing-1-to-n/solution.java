// ──────────────────────────────────────────────────
// Problem  : 1016. Binary String With Substrings Representing 1 To N
// Difficulty: Medium
// Tags     : Hash Table, String, Bit Manipulation, Sliding Window
// Link     : https://leetcode.com/problems/binary-string-with-substrings-representing-1-to-n/
// Runtime  : 0 ms (beats 100%)
// Memory   : 42696000 (beats 67%)
// Language : java
// Copyright: (c) 2026 gayathri16006. All rights reserved.
// Synced by: leetie
// ──────────────────────────────────────────────────

class Solution {
    public boolean queryString(String s, int n) {
        // A string of length <= 1000 cannot contain all binary representations for n > 2048
        if (n > 2048) {
            return false;
        }

        // Checking from n down to n / 2 is sufficient because
        // any x has x / 2 as a prefix in binary.
        for (int i = n; i > n / 2; i--) {
            if (!s.contains(Integer.toBinaryString(i))) {
                return false;
            }
        }

        return true;
    }
}