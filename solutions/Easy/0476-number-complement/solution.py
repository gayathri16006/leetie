# ──────────────────────────────────────────────────
# Problem  : 476. Number Complement
# Difficulty: Easy
# Tags     : Bit Manipulation
# Link     : https://leetcode.com/problems/number-complement/
# Runtime  : 0 ms (beats 100%)
# Memory   : 12224000 (beats 88%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):

    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        # Create a bitmask with all 1s having the same bit-length as num
        mask = (1 << num.bit_length()) - 1

        # XOR num with the mask to flip all bits
        return num ^ mask