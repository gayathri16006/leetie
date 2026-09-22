// ──────────────────────────────────────────────────
// Problem  : 1137. N-th Tribonacci Number
// Difficulty: Easy
// Tags     : Math, Dynamic Programming, Memoization
// Link     : https://leetcode.com/problems/n-th-tribonacci-number/
// Runtime  : 0 ms (beats 100%)
// Memory   : 42284000 (beats 16%)
// Language : java
// Copyright: (c) 2026 gayathri16006. All rights reserved.
// Synced by: leetie
// ──────────────────────────────────────────────────

class Solution {
    public int tribonacci(int n) {
        if (n == 0) return 0;
        if (n == 1 || n == 2) return 1;

        int a = 0; 
        int b = 1; 
        int c = 1; 

        for (int i = 3; i <= n; i++) {
            int next = a + b + c;
            a = b;
            b = c;
            c = next;
        }

        return c;
    }
}