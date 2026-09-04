# ──────────────────────────────────────────────────
# Problem  : 898. Bitwise ORs of Subarrays
# Difficulty: Medium
# Tags     : Array, Dynamic Programming, Bit Manipulation
# Link     : https://leetcode.com/problems/bitwise-ors-of-subarrays/
# Runtime  : 603 ms (beats 30%)
# Memory   : 36408000 (beats 68%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def subarrayBitwiseORs(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        res = set()
        cur = set()

        for x in arr:
            # Subarrays ending at x are either [x] itself or (subarrays ending at previous index) | x
            cur = {x | y for y in cur} | {x}
            res |= cur

        return len(res)