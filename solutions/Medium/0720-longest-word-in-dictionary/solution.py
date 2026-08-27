# ──────────────────────────────────────────────────
# Problem  : 720. Longest Word in Dictionary
# Difficulty: Medium
# Tags     : Array, Hash Table, String, Trie, Sorting
# Link     : https://leetcode.com/problems/longest-word-in-dictionary/
# Runtime  : 5 ms (beats 86%)
# Memory   : 19552000 (beats 55%)
# Language : python3
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def longestWord(self, words: list[str]) -> str:
        # Sort lexicographically first so the earliest valid word of max length is preferred
        words.sort()
        
        built = {""}
        longest = ""
        
        for word in words:
            # Check if prefix of length len(word) - 1 can be built
            if word[:-1] in built:
                built.add(word)
                if len(word) > len(longest):
                    longest = word
                    
        return longest