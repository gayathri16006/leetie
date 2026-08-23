# ──────────────────────────────────────────────────
# Problem  : 557. Reverse Words in a String III
# Difficulty: Easy
# Tags     : Two Pointers, String
# Link     : https://leetcode.com/problems/reverse-words-in-a-string-iii/
# Runtime  : 0 ms (beats 100%)
# Memory   : 12764000 (beats 84%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def reverseWords(self, s):
        return " ".join(word[::-1] for word in s.split(" "))