# ──────────────────────────────────────────────────
# Problem  : 745. Prefix and Suffix Search
# Difficulty: Hard
# Tags     : Array, Hash Table, String, Design, Trie
# Link     : https://leetcode.com/problems/prefix-and-suffix-search/
# Runtime  : 656 ms (beats 73%)
# Memory   : 98920000 (beats 50%)
# Language : python3
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class WordFilter:

    def __init__(self, words: list[str]):
        # Map every possible (prefix, suffix) combination to its largest index
        self.lookup = {}
        for index, word in enumerate(words):
            n = len(word)
            # Generate all possible prefixes (length 0 to n) and suffixes (length 0 to n)
            for i in range(n + 1):
                pref = word[:i]
                for j in range(n + 1):
                    suff = word[j:]
                    self.lookup[(pref, suff)] = index

    def f(self, pref: str, suff: str) -> int:
        return self.lookup.get((pref, suff), -1)