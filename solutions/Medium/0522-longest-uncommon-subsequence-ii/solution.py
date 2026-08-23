# ──────────────────────────────────────────────────
# Problem  : 522. Longest Uncommon Subsequence II
# Difficulty: Medium
# Tags     : Array, Hash Table, Two Pointers, String, Sorting
# Link     : https://leetcode.com/problems/longest-uncommon-subsequence-ii/
# Runtime  : 0 ms (beats 0%)
# Memory   : 12552000 (beats 0%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def findLUSlength(self, strs):
        def is_subsequence(s1, s2):
            """Check if s1 is a subsequence of s2."""
            i, j = 0, 0
            while i < len(s1) and j < len(s2):
                if s1[i] == s2[j]:
                    i += 1
                j += 1
            return i == len(s1)

        # Sort strings by length in descending order
        strs.sort(key=len, reverse=True)
        
        for i, s1 in enumerate(strs):
            all_uncommon = True
            for j, s2 in enumerate(strs):
                if i == j:
                    continue
                if is_subsequence(s1, s2):
                    all_uncommon = False
                    break
            if all_uncommon:
                return len(s1)
                
        return -1