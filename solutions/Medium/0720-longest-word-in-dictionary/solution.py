# ──────────────────────────────────────────────────
# Problem  : 720. Longest Word in Dictionary
# Difficulty: Medium
# Tags     : Array, Hash Table, String, Trie, Sorting
# Link     : https://leetcode.com/problems/longest-word-in-dictionary/
# Runtime  : 7 ms (beats 80%)
# Memory   : 19628000 (beats 43%)
# Language : python3
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def longestWord(self, words: list[str]) -> str:
        # Sort words lexicographically first
        words.sort()
        
        built = {""}
        longest = ""
        
        for word in words:
            # Check if prefix of length len(word) - 1 exists
            if word[:-1] in built:
                built.add(word)
                if len(word) > len(longest):
                    longest = word
                    
        return longest