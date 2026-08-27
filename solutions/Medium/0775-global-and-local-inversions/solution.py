# ──────────────────────────────────────────────────
# Problem  : 775. Global and Local Inversions
# Difficulty: Medium
# Tags     : Array, Math
# Link     : https://leetcode.com/problems/global-and-local-inversions/
# Runtime  : 0 ms (beats 0%)
# Memory   : 19036000 (beats 0%)
# Language : python3
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def isIdealPermutation(self, nums: list[int]) -> bool:
        # Every local inversion is also a global inversion.
        # The two counts are equal if and only if there are no non-local global inversions.
        # Since nums is a permutation of [0, n - 1], every element can move at most 1 step away from its sorted index.
        for i, val in enumerate(nums):
            if abs(val - i) > 1:
                return False
                
        return True