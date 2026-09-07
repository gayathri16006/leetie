# ──────────────────────────────────────────────────
# Problem  : 921. Minimum Add to Make Parentheses Valid
# Difficulty: Medium
# Tags     : String, Stack, Greedy, Bracket Sequences
# Link     : https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/
# Runtime  : 0 ms (beats 100%)
# Memory   : 12412000 (beats 19%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        open_needed = 0
        close_needed = 0

        for char in s:
            if char == '(':
                open_needed += 1
            elif char == ')':
                if open_needed > 0:
                    open_needed -= 1
                else:
                    close_needed += 1

        return open_needed + close_needed