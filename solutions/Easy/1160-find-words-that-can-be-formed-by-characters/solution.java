// ──────────────────────────────────────────────────
// Problem  : 1160. Find Words That Can Be Formed by Characters
// Difficulty: Easy
// Tags     : Array, Hash Table, String, Counting
// Link     : https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/
// Runtime  : 0 ms (beats 0%)
// Memory   : 42836000 (beats 0%)
// Language : java
// Copyright: (c) 2026 gayathri16006. All rights reserved.
// Synced by: leetie
// ──────────────────────────────────────────────────

class Solution {
    public int countCharacters(String[] words, String chars) {
        int[] charCounts = new int[26];
        for (char c : chars.toCharArray()) {
            charCounts[c - 'a']++;
        }

        int totalLength = 0;

        for (String word : words) {
            int[] wordCounts = new int[26];
            boolean canForm = true;

            for (char c : word.toCharArray()) {
                int idx = c - 'a';
                wordCounts[idx]++;
                if (wordCounts[idx] > charCounts[idx]) {
                    canForm = false;
                    break;
                }
            }

            if (canForm) {
                totalLength += word.length();
            }
        }

        return totalLength;
    }
}