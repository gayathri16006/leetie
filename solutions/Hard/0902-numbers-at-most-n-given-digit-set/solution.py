# ──────────────────────────────────────────────────
# Problem  : 902. Numbers At Most N Given Digit Set
# Difficulty: Hard
# Tags     : Array, Math, String, Binary Search, Dynamic Programming
# Link     : https://leetcode.com/problems/numbers-at-most-n-given-digit-set/
# Runtime  : 0 ms (beats 0%)
# Memory   : 12572000 (beats 0%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def atMostNGivenDigitSet(self, digits, n):
        """
        :type digits: List[str]
        :type n: int
        :rtype: int
        """
        s = str(n)
        L = len(s)
        num_digits = len(digits)
        
        # Step 1: Count numbers with length < L
        total = sum(num_digits ** k for k in range(1, L))

        # Step 2: Count numbers with length == L
        for i, char in enumerate(s):
            # Digits strictly smaller than s[i]
            smaller_count = sum(1 for d in digits if d < char)
            total += smaller_count * (num_digits ** (L - 1 - i))

            # If the current digit cannot match s[i], terminate
            if char not in digits:
                break
        else:
            # If the loop finished without breaking, n itself is valid
            total += 1

        return total