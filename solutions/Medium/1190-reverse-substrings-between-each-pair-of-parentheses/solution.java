// ──────────────────────────────────────────────────
// Problem  : 1190. Reverse Substrings Between Each Pair of Parentheses
// Difficulty: Medium
// Tags     : String, Stack, Bracket Sequences
// Link     : https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/
// Runtime  : 1 ms (beats 100%)
// Memory   : 42760000 (beats 95%)
// Language : java
// Copyright: (c) 2026 gayathri16006. All rights reserved.
// Synced by: leetie
// ──────────────────────────────────────────────────

class Solution {
    public String reverseParentheses(String s) {
        int n = s.length();
        int[] pair = new int[n];
        int[] stack = new int[n];
        int top = -1;

        // Step 1: Pair up matching parentheses
        for (int i = 0; i < n; i++) {
            char c = s.charAt(i);
            if (c == '(') {
                stack[++top] = i;
            } else if (c == ')') {
                int j = stack[top--];
                pair[i] = j;
                pair[j] = i;
            }
        }

        // Step 2: Traverse using the wormhole/teleportation approach
        StringBuilder sb = new StringBuilder();
        int dir = 1; // 1 for moving right, -1 for moving left

        for (int i = 0; i < n && i >= 0; i += dir) {
            char c = s.charAt(i);
            if (c == '(' || c == ')') {
                i = pair[i];
                dir = -dir;
            } else {
                sb.append(c);
            }
        }

        return sb.toString();
    }
}