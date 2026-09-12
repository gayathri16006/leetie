# ──────────────────────────────────────────────────
# Problem  : 914. X of a Kind in a Deck of Cards
# Difficulty: Easy
# Tags     : Array, Hash Table, Math, Counting, Number Theory, Euclidean Algorithm, Greatest Common Divisor
# Link     : https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards/
# Runtime  : 7 ms (beats 80%)
# Memory   : 12648000 (beats 48%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

from collections import Counter
from fractions import gcd

class Solution(object):
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        counts = Counter(deck).values()
        common_gcd = reduce(gcd, counts)
        return common_gcd >= 2