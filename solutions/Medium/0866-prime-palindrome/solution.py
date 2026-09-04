# ──────────────────────────────────────────────────
# Problem  : 866. Prime Palindrome
# Difficulty: Medium
# Tags     : Math, Number Theory, Primality Test
# Link     : https://leetcode.com/problems/prime-palindrome/
# Runtime  : 88 ms (beats 64%)
# Memory   : 15224000 (beats 35%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def primePalindrome(self, n):
        """
        :type n: int
        :rtype: int
        """
        def is_prime(x):
            if x < 2:
                return False
            if x % 2 == 0:
                return x == 2
            d = 3
            while d * d <= x:
                if x % d == 0:
                    return False
                d += 2
            return True

        # Special case: 11 is the only even-length prime palindrome
        if 8 <= n <= 11:
            return 11

        # Generate odd-length palindromes from 1 to 5 digits root (1 to 20000)
        # Root L creates an odd palindrome of length 2*len(L) - 1 (up to 9 digits, ~2*10^8)
        for length in range(1, 6):
            start = 10**(length - 1)
            end = 10**length
            for root in range(start, end):
                s = str(root)
                # Form odd-length palindrome: root + reversed(root[:-1])
                val = int(s + s[-2::-1])
                if val >= n and is_prime(val):
                    return val

        return -1