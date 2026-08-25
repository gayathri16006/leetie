# ──────────────────────────────────────────────────
# Problem  : 693. Binary Number with Alternating Bits
# Difficulty: Easy
# Tags     : Bit Manipulation
# Link     : https://leetcode.com/problems/binary-number-with-alternating-bits/
# Runtime  : 0 ms (beats 0%)
# Memory   : 19168000 (beats 0%)
# Language : python3
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        # If n has alternating bits, (n ^ (n >> 1)) produces all 1s (e.g., 101 ^ 010 = 111)
        temp = n ^ (n >> 1)
        
        # A number with all 1s satisfies: temp & (temp + 1) == 0 (e.g., 111 & 1000 = 0)
        return (temp & (temp + 1)) == 0