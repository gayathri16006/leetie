# ──────────────────────────────────────────────────
# Problem  : 819. Most Common Word
# Difficulty: Easy
# Tags     : Array, Hash Table, String, Counting
# Link     : https://leetcode.com/problems/most-common-word/
# Runtime  : 0 ms (beats 0%)
# Memory   : 12244000 (beats 0%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

import collections
import re

class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        banned_set = set(banned)
        # Extract only lowercase alphanumeric words using regex
        words = re.findall(r'\w+', paragraph.lower())
        
        # Count frequencies of words that are not in the banned set
        count = collections.Counter(word for word in words if word not in banned_set)
        
        # Return the most common non-banned word
        return count.most_common(1)[0][0]