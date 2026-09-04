# ──────────────────────────────────────────────────
# Problem  : 843. Guess the Word
# Difficulty: Hard
# Tags     : Array, Math, String, Minimax, Interactive, Game Theory
# Link     : https://leetcode.com/problems/guess-the-word/
# Runtime  : 16 ms (beats 0%)
# Memory   : 12340000 (beats 0%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def findSecretWord(self, words, master):
        """
        :type words: List[Str]
        :type master: Master
        :rtype: None
        """
        def get_matches(w1, w2):
            return sum(c1 == c2 for c1, c2 in zip(w1, w2))

        candidates = list(words)

        while candidates:
            # Minimax choice: pick candidate that minimizes the maximum group size
            best_word = None
            min_max_group = float('inf')

            for w1 in candidates:
                counts = [0] * 7
                for w2 in candidates:
                    if w1 != w2:
                        counts[get_matches(w1, w2)] += 1
                
                max_group = max(counts)
                if max_group < min_max_group:
                    min_max_group = max_group
                    best_word = w1

            matches = master.guess(best_word)
            if matches == 6:
                return

            # Keep only words with the exact same match count
            candidates = [w for w in candidates if get_matches(best_word, w) == matches]