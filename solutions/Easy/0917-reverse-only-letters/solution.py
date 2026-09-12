# ──────────────────────────────────────────────────
# Problem  : 917. Reverse Only Letters
# Difficulty: Easy
# Tags     : Two Pointers, String
# Link     : https://leetcode.com/problems/reverse-only-letters/
# Runtime  : 1 ms (beats 20%)
# Memory   : 12472000 (beats 17%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def reverseOnlyLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        chars = list(s)
        left, right = 0, len(chars) - 1

        while left < right:
            if not chars[left].isalpha():
                left += 1
            elif not chars[right].isalpha():
                right -= 1
            else:
                chars[left], chars[right] = chars[right], chars[left]
                left += 1
                right -= 1

        return "".join(chars)