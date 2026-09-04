# ──────────────────────────────────────────────────
# Problem  : 890. Find and Replace Pattern
# Difficulty: Medium
# Tags     : Array, Hash Table, String
# Link     : https://leetcode.com/problems/find-and-replace-pattern/
# Runtime  : 2 ms (beats 30%)
# Memory   : 12164000 (beats 100%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        def matches(word):
            # Check bijection using two hash maps
            w_to_p = {}
            p_to_w = {}

            for w, p in zip(word, pattern):
                if w not in w_to_p:
                    w_to_p[w] = p
                if p not in p_to_w:
                    p_to_w[p] = w

                if w_to_p[w] != p or p_to_w[p] != w:
                    return False

            return True

        return [word for word in words if matches(word)]