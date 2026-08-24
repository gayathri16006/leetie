# ──────────────────────────────────────────────────
# Problem  : 520. Detect Capital
# Difficulty: Easy
# Tags     : String
# Link     : https://leetcode.com/problems/detect-capital/
# Runtime  : 0 ms (beats 100%)
# Memory   : 12260000 (beats 89%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        return word.isupper() or word.islower() or word.istitle()