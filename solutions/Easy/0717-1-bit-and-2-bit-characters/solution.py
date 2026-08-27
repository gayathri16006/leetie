# ──────────────────────────────────────────────────
# Problem  : 717. 1-bit and 2-bit Characters
# Difficulty: Easy
# Tags     : Array
# Link     : https://leetcode.com/problems/1-bit-and-2-bit-characters/
# Runtime  : 0 ms (beats 100%)
# Memory   : 19232000 (beats 53%)
# Language : python3
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def isOneBitCharacter(self, bits: list[int]) -> bool:
        i = len(bits) - 2
        while i >= 0 and bits[i] == 1:
            i -= 1
        return (len(bits) - 2 - i) % 2 == 0