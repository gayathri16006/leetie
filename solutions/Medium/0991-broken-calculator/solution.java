// ──────────────────────────────────────────────────
// Problem  : 991. Broken Calculator
// Difficulty: Medium
// Tags     : Math, Greedy
// Link     : https://leetcode.com/problems/broken-calculator/
// Runtime  : 0 ms (beats 100%)
// Memory   : 41956000 (beats 80%)
// Language : java
// Copyright: (c) 2026 gayathri16006. All rights reserved.
// Synced by: leetie
// ──────────────────────────────────────────────────

class Solution {
    public int brokenCalc(int startValue, int target) {
        int operations = 0;

        while (target > startValue) {
            operations++;
            if (target % 2 == 1) {
                target++;
            } else {
                target /= 2;
            }
        }

        
        return operations + (startValue - target);
    }
}