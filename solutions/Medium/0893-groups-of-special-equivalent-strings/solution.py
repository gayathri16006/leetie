# ──────────────────────────────────────────────────
# Problem  : 893. Groups of Special-Equivalent Strings
# Difficulty: Medium
# Tags     : Array, Hash Table, String, Sorting
# Link     : https://leetcode.com/problems/groups-of-special-equivalent-strings/
# Runtime  : 2 ms (beats 100%)
# Memory   : 12388000 (beats 96%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def numSpecialEquivGroups(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        seen = set()

        for word in words:
            # Separate and sort even and odd indexed characters
            even_sorted = "".join(sorted(word[0::2]))
            odd_sorted = "".join(sorted(word[1::2]))
            
            seen.add((even_sorted, odd_sorted))

        return len(seen)