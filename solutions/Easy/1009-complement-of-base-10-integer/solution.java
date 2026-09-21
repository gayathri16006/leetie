// ──────────────────────────────────────────────────
// Problem  : 1009. Complement of Base 10 Integer
// Difficulty: Easy
// Tags     : Bit Manipulation
// Link     : https://leetcode.com/problems/complement-of-base-10-integer/
// Runtime  : 0 ms (beats 0%)
// Memory   : 42008000 (beats 0%)
// Language : java
// Copyright: (c) 2026 gayathri16006. All rights reserved.
// Synced by: leetie
// ──────────────────────────────────────────────────

class Solution {
    public int bitwiseComplement(int n) {
        if (n == 0) return 1;

        int mask = 1;
        while (mask < n) {
            mask = (mask << 1) | 1;
        }

        return n ^ mask;
    }
}