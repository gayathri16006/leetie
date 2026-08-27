# ──────────────────────────────────────────────────
# Problem  : 792. Number of Matching Subsequences
# Difficulty: Medium
# Tags     : Array, Hash Table, String, Binary Search, Dynamic Programming, Trie, Sorting
# Link     : https://leetcode.com/problems/number-of-matching-subsequences/
# Runtime  : 204 ms (beats 87%)
# Memory   : 21072000 (beats 71%)
# Language : python3
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

from collections import defaultdict

class Solution:
    def numMatchingSubseq(self, s: str, words: list[str]) -> int:
        # Group word iterators by the character they are currently waiting for
        waiting = defaultdict(list)
        for word in words:
            it = iter(word)
            waiting[next(it)].append(it)
            
        count = 0
        for char in s:
            # Retrieve and clear the list of iterators waiting for the current character
            current_bucket = waiting[char]
            waiting[char] = []
            
            for it in current_bucket:
                next_char = next(it, None)
                if next_char is None:
                    # Completed matching all characters in the word
                    count += 1
                else:
                    # Advance to the bucket for the next waiting character
                    waiting[next_char].append(it)
                    
        return count