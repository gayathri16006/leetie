# ──────────────────────────────────────────────────
# Problem  : 479. Largest Palindrome Product
# Difficulty: Hard
# Tags     : Math, Enumeration
# Link     : https://leetcode.com/problems/largest-palindrome-product/
# Runtime  : 0 ms (beats 0%)
# Memory   : 12420000 (beats 0%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):

    def largestPalindrome(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Special base case for single digit
        if n == 1:
            return 9

        upper = 10**n - 1
        lower = 10 ** (n - 1)

        # Iterate down from the largest possible left-half of a 2n-digit palindrome
        for left in range(upper, lower - 1, -1):
            # Form the even-length palindrome by mirroring the left half
            palindrome = int(str(left) + str(left)[::-1])

            # Check if palindrome can be factored into two n-digit numbers
            d = upper
            while d * d >= palindrome:
                if palindrome % d == 0:
                    other_factor = palindrome // d
                    if lower <= other_factor <= upper:
                        return palindrome % 1337
                d -= 1

        return 0