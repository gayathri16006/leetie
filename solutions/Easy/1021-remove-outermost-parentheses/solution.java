// ──────────────────────────────────────────────────
// Problem  : 1021. Remove Outermost Parentheses
// Difficulty: Easy
// Tags     : String, Stack, Bracket Sequences
// Link     : https://leetcode.com/problems/remove-outermost-parentheses/
// Runtime  : 0 ms (beats 0%)
// Memory   : 42672000 (beats 0%)
// Language : java
// Copyright: (c) 2026 gayathri16006. All rights reserved.
// Synced by: leetie
// ──────────────────────────────────────────────────

class Solution {
    public String removeOuterParentheses(String s) {
        StringBuilder sb = new StringBuilder();
        int opened = 0;

        for (char c : s.toCharArray()) {
            if (c == '(') {
                if (opened > 0) {
                    sb.append(c);
                }
                opened++;
            } else {
                opened--;
                if (opened > 0) {
                    sb.append(c);
                }
            }
        }

        return sb.toString();
    }
}