# ──────────────────────────────────────────────────
# Problem  : 467. Unique Substrings in Wraparound String
# Difficulty: Medium
# Tags     : String, Dynamic Programming
# Link     : https://leetcode.com/problems/unique-substrings-in-wraparound-string/
# Runtime  : 71 ms (beats 49%)
# Memory   : 15464000 (beats 56%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def findSubstringInWraproundString(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        # max_len[c] stores the max length of contiguous substring ending with character c
        max_len = collections.defaultdict(int)
        
        current_len = 0

        for i in range(len(s)):
            # Check if s[i] follows s[i-1] cyclically ('z' -> 'a' or diff == 1)
            if i > 0 and (ord(s[i]) - ord(s[i - 1]) == 1 or (s[i - 1] == 'z' and s[i] == 'a')):
                current_len += 1
            else:
                current_len = 1

            # Update the maximum valid substring length ending with s[i]
            max_len[s[i]] = max(max_len[s[i]], current_len)

        return sum(max_len.values())