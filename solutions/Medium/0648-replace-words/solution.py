# ──────────────────────────────────────────────────
# Problem  : 648. Replace Words
# Difficulty: Medium
# Tags     : Array, Hash Table, String, Trie
# Link     : https://leetcode.com/problems/replace-words/
# Runtime  : 42 ms (beats 71%)
# Memory   : 35616000 (beats 16%)
# Language : python3
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        root = TrieNode()
        
        # Build Trie from dictionary roots
        for word in dictionary:
            node = root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.is_end = True
            
        def find_root(word: str) -> str:
            node = root
            for i, ch in enumerate(word):
                if ch not in node.children:
                    break
                node = node.children[ch]
                if node.is_end:
                    # Return shortest matching root prefix
                    return word[:i + 1]
            return word

        words = sentence.split(" ")
        return " ".join(find_root(w) for w in words)