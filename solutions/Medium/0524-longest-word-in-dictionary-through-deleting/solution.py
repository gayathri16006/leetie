# ──────────────────────────────────────────────────
# Problem  : 524. Longest Word in Dictionary through Deleting
# Difficulty: Medium
# Tags     : Array, Two Pointers, String, Sorting
# Link     : https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/
# Runtime  : 367 ms (beats 46%)
# Memory   : 14264000 (beats 10%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def findLongestWord(self, s, dictionary):
        def is_subsequence(word, target):
            i, j = 0, 0
            while i < len(word) and j < len(target):
                if word[i] == target[j]:
                    i += 1
                j += 1
            return i == len(word)

        # Sort by: -len(word) (longest first), then word (alphabetical)
        dictionary.sort(key=lambda w: (-len(w), w))

        for word in dictionary:
            if is_subsequence(word, s):
                return word

        return ""