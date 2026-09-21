// ──────────────────────────────────────────────────
// Problem  : 1003. Check If Word Is Valid After Substitutions
// Difficulty: Medium
// Tags     : String, Stack
// Link     : https://leetcode.com/problems/check-if-word-is-valid-after-substitutions/
// Runtime  : 0 ms (beats 0%)
// Memory   : 42696000 (beats 0%)
// Language : java
// Copyright: (c) 2026 gayathri16006. All rights reserved.
// Synced by: leetie
// ──────────────────────────────────────────────────

class Solution {
    public boolean isValid(String s) {
        char[] stack = new char[s.length()];
        int top = 0;

        for (char c : s.toCharArray()) {
            stack[top++] = c;
            
            
            if (top >= 3 && stack[top - 3] == 'a' && stack[top - 2] == 'b' && stack[top - 1] == 'c') {
                top -= 3;
            }
        }

        return top == 0;
    }
}