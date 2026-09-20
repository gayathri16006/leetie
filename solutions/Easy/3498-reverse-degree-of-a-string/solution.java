// ──────────────────────────────────────────────────
// Problem  : 3498. Reverse Degree of a String
// Difficulty: Easy
// Tags     : String, Simulation
// Link     : https://leetcode.com/problems/reverse-degree-of-a-string/
// Runtime  : 1 ms (beats 100%)
// Memory   : 44172000 (beats 34%)
// Language : java
// Copyright: (c) 2026 gayathri16006. All rights reserved.
// Synced by: leetie
// ──────────────────────────────────────────────────

class Solution {
    public int reverseDegree(String s) {
        int total = 0;
        for (int i = 0; i < s.length(); i++) {
            int charValue = 26 - (s.charAt(i) - 'a');
            total += charValue * (i + 1);
        }
        return total;
    }
}