// ──────────────────────────────────────────────────
// Problem  : 984. String Without AAA or BBB
// Difficulty: Medium
// Tags     : String, Greedy
// Link     : https://leetcode.com/problems/string-without-aaa-or-bbb/
// Runtime  : 0 ms (beats 0%)
// Memory   : 42796000 (beats 0%)
// Language : java
// Copyright: (c) 2026 gayathri16006. All rights reserved.
// Synced by: leetie
// ──────────────────────────────────────────────────

class Solution {
    public String strWithout3a3b(int a, int b) {
        StringBuilder sb = new StringBuilder();

        while (a > 0 || b > 0) {
            boolean writeA = false;
            int len = sb.length();

            // If the last two characters are 'b', we must append 'a'
            if (len >= 2 && sb.charAt(len - 1) == 'b' && sb.charAt(len - 2) == 'b') {
                writeA = true;
            // If the last two characters are 'a', we must append 'b'
            } else if (len >= 2 && sb.charAt(len - 1) == 'a' && sb.charAt(len - 2) == 'a') {
                writeA = false;
            // Otherwise, pick the character with the larger remaining count
            } else {
                writeA = a >= b;
            }

            if (writeA) {
                sb.append('a');
                a--;
            } else {
                sb.append('b');
                b--;
            }
        }

        return sb.toString();
    }
}