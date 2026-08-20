# ──────────────────────────────────────────────────
# Problem  : 400. Nth Digit
# Difficulty: Medium
# Tags     : Math, Binary Search
# Link     : https://leetcode.com/problems/nth-digit/
# Runtime  : 0 ms (beats 100%)
# Memory   : 12428000 (beats 17%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        length = 1     
        count = 9      
        start = 1       # First number of the current digit group (1, 10, 100, ...)

        # Step 1: Find the digit group that contains the n-th digit
        while n > length * count:
            n -= length * count
            length += 1
            count *= 10
            start *= 10

        # Step 2: Identify the exact number
        target_number = start + (n - 1) // length

        # Step 3: Find the exact digit within target_number
        digit_index = (n - 1) % length
        return int(str(target_number)[digit_index])