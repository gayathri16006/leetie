# ──────────────────────────────────────────────────
# Problem  : 28. Find the Index of the First Occurrence in a String
# Difficulty: Easy
# Tags     : Two Pointers, String, String Matching, Z Algorithm, Knuth–Morris–Pratt Algorithm, Boyer–Moore String-Search Algorithm
# Link     : https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
# Runtime  : 4 ms (beats 9%)
# Memory   : 19544000 (beats 8%)
# Language : python3
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def strStr(self, haystack, needle):
        m = len(needle)
        lps = [0] * m

        j = 0
        for i in range(1, m):
            while j > 0 and needle[i] != needle[j]:
                j = lps[j - 1]

            if needle[i] == needle[j]:
                j += 1

            lps[i] = j

        i = j = 0

        while i < len(haystack):
            if haystack[i] == needle[j]:
                i += 1
                j += 1

                if j == m:
                    return i - j
            else:
                if j > 0:
                    j = lps[j - 1]
                else:
                    i += 1

        return -1