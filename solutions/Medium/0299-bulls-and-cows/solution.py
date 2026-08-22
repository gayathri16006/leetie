# ──────────────────────────────────────────────────
# Problem  : 299. Bulls and Cows
# Difficulty: Medium
# Tags     : Hash Table, String, Counting
# Link     : https://leetcode.com/problems/bulls-and-cows/
# Runtime  : 7 ms (beats 88%)
# Memory   : 12524000 (beats 4%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

from collections import Counter

class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        bulls = 0
        secret_remain = []
        guess_remain = []
        
        # Step 1: Count bulls (exact matches at the same index)
        for s, g in zip(secret, guess):
            if s == g:
                bulls += 1
            else:
                secret_remain.append(s)
                guess_remain.append(g)
        
        # Step 2: Count cows from remaining non-bull digits
        secret_counts = Counter(secret_remain)
        guess_counts = Counter(guess_remain)
        
        cows = 0
        for digit in guess_counts:
            if digit in secret_counts:
                cows += min(guess_counts[digit], secret_counts[digit])
                
        return "{}A{}B".format(bulls, cows)