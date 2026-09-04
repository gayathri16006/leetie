# ──────────────────────────────────────────────────
# Problem  : 844. Backspace String Compare
# Difficulty: Easy
# Tags     : Two Pointers, String, Stack, Simulation
# Link     : https://leetcode.com/problems/backspace-string-compare/
# Runtime  : 0 ms (beats 100%)
# Memory   : 12428000 (beats 21%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        i = len(s) - 1
        j = len(t) - 1

        skip_s = 0
        skip_t = 0

        while i >= 0 or j >= 0:
            # Find next valid character in s
            while i >= 0:
                if s[i] == '#':
                    skip_s += 1
                    i -= 1
                elif skip_s > 0:
                    skip_s -= 1
                    i -= 1
                else:
                    break

            # Find next valid character in t
            while j >= 0:
                if t[j] == '#':
                    skip_t += 1
                    j -= 1
                elif skip_t > 0:
                    skip_t -= 1
                    j -= 1
                else:
                    break

            # Compare current characters
            if i >= 0 and j >= 0:
                if s[i] != t[j]:
                    return False
            elif i >= 0 or j >= 0:
                # One string ended while the other still has valid characters
                return False

            i -= 1
            j -= 1

        return True