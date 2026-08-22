# ──────────────────────────────────────────────────
# Problem  : 500. Keyboard Row
# Difficulty: Easy
# Tags     : Array, Hash Table, String
# Link     : https://leetcode.com/problems/keyboard-row/
# Runtime  : 0 ms (beats 100%)
# Memory   : 12500000 (beats 21%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")

        valid_words = []
        for word in words:
            word_chars = set(word.lower())
            if word_chars <= row1 or word_chars <= row2 or word_chars <= row3:
                valid_words.append(word)

        return valid_words