# ──────────────────────────────────────────────────
# Problem  : 906. Super Palindromes
# Difficulty: Hard
# Tags     : Math, String, Enumeration
# Link     : https://leetcode.com/problems/super-palindromes/
# Runtime  : 483 ms (beats 82%)
# Memory   : 15524000 (beats 39%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def superpalindromesInRange(self, left, right):
        """
        :type left: str
        :type right: str
        :rtype: int
        """
        L = int(left)
        R = int(right)
        ans = 0

        def is_palindrome(n):
            s = str(n)
            return s == s[::-1]

        # Generate odd-length palindromic roots: e.g., k = 123 -> 12321
        for k in range(1, 100000):
            s = str(k)
            pal_str = s + s[-2::-1]
            val = int(pal_str)
            square = val * val
            if square > R:
                break
            if square >= L and is_palindrome(square):
                ans += 1

        # Generate even-length palindromic roots: e.g., k = 123 -> 123321
        for k in range(1, 100000):
            s = str(k)
            pal_str = s + s[::-1]
            val = int(pal_str)
            square = val * val
            if square > R:
                break
            if square >= L and is_palindrome(square):
                ans += 1

        return ans