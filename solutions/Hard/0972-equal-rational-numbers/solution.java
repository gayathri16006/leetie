// ──────────────────────────────────────────────────
// Problem  : 972. Equal Rational Numbers
// Difficulty: Hard
// Tags     : Math, String
// Link     : https://leetcode.com/problems/equal-rational-numbers/
// Runtime  : 3 ms (beats 37%)
// Memory   : 44556000 (beats 6%)
// Language : java
// Copyright: (c) 2026 gayathri16006. All rights reserved.
// Synced by: leetie
// ──────────────────────────────────────────────────

class Solution {
    public boolean isRationalEqual(String s, String t) {
        return Math.abs(valueOf(s) - valueOf(t)) < 1e-9;
    }

    private double valueOf(String s) {
        int openParen = s.indexOf('(');
        if (openParen == -1) {
            return Double.parseDouble(s);
        }

        String nonRepeating = s.substring(0, openParen);
        String repeating = s.substring(openParen + 1, s.length() - 1);

        StringBuilder sb = new StringBuilder(nonRepeating);
       
        while (sb.length() < 20) {
            sb.append(repeating);
        }

        return Double.parseDouble(sb.toString());
    }
}