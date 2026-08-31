# ──────────────────────────────────────────────────
# Problem  : 214. Shortest Palindrome
# Difficulty: Hard
# Tags     : String, Rolling Hash, String Matching, Hash Function, Manacher, Z Algorithm, Knuth–Morris–Pratt Algorithm
# Link     : https://leetcode.com/problems/shortest-palindrome/
# Runtime  : 43 ms (beats 81%)
# Memory   : 23288000 (beats 55%)
# Language : python3
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def shortestPalindrome(self, s):
        rev = s[::-1]
        combined = s + "#" + rev

        lps = [0] * len(combined)
        j = 0

        for i in range(1, len(combined)):
            while j > 0 and combined[i] != combined[j]:
                j = lps[j - 1]

            if combined[i] == combined[j]:
                j += 1

            lps[i] = j

        longest = lps[-1]

        return rev[:len(s) - longest] + s