# ──────────────────────────────────────────────────
# Problem  : 880. Decoded String at Index
# Difficulty: Medium
# Tags     : String, Stack
# Link     : https://leetcode.com/problems/decoded-string-at-index/
# Runtime  : 0 ms (beats 0%)
# Memory   : 12496000 (beats 0%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def decodeAtIndex(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        size = 0

        # Step 1: Compute the length of the decoded string
        for ch in s:
            if ch.isdigit():
                size *= int(ch)
            else:
                size += 1

        # Step 2: Traverse backwards to find the k-th character
        for ch in reversed(s):
            k %= size

            if k == 0 and ch.isalpha():
                return ch

            if ch.isdigit():
                size //= int(ch)
            else:
                size -= 1

        return ""