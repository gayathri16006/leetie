# ──────────────────────────────────────────────────
# Problem  : 916. Word Subsets
# Difficulty: Medium
# Tags     : Array, Hash Table, String
# Link     : https://leetcode.com/problems/word-subsets/
# Runtime  : 833 ms (beats 43%)
# Memory   : 15888000 (beats 72%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

from collections import Counter

class Solution(object):
    def wordSubsets(self, words1, words2):
        """
        :type words1: List[str]
        :type words2: List[str]
        :rtype: List[str]
        """
        # Step 1: Find the max frequency needed for each char across all words in words2
        max_freq = Counter()
        for b in words2:
            b_count = Counter(b)
            for char, count in b_count.items():
                max_freq[char] = max(max_freq[char], count)

        # Step 2: Check each word in words1 against the combined frequency requirement
        ans = []
        for a in words1:
            a_count = Counter(a)
            if all(a_count[char] >= max_freq[char] for char in max_freq):
                ans.append(a)

        return ans