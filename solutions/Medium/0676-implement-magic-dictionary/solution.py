# ──────────────────────────────────────────────────
# Problem  : 676. Implement Magic Dictionary
# Difficulty: Medium
# Tags     : Hash Table, String, Depth-First Search, Design, Trie
# Link     : https://leetcode.com/problems/implement-magic-dictionary/
# Runtime  : 11 ms (beats 88%)
# Memory   : 19588000 (beats 93%)
# Language : python3
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

from collections import defaultdict
from typing import List

class MagicDictionary:

    def __init__(self):
        # Group words by their lengths to quickly filter out invalid candidates
        self.words_by_len = defaultdict(list)

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            self.words_by_len[len(word)].append(word)

    def search(self, searchWord: str) -> bool:
        n = len(searchWord)
        
        # Only evaluate candidates of the exact same length
        for candidate in self.words_by_len[n]:
            diff_count = 0
            
            for c1, c2 in zip(searchWord, candidate):
                if c1 != c2:
                    diff_count += 1
                    if diff_count > 1:
                        break
                        
            # Valid only if exactly one character differs
            if diff_count == 1:
                return True
                
        return False