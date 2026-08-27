# ──────────────────────────────────────────────────
# Problem  : 747. Largest Number At Least Twice of Others
# Difficulty: Easy
# Tags     : Array, Sorting
# Link     : https://leetcode.com/problems/largest-number-at-least-twice-of-others/
# Runtime  : 0 ms (beats 100%)
# Memory   : 19116000 (beats 86%)
# Language : python3
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def dominantIndex(self, nums: list[int]) -> int:
        max_val = -1
        second_max = -1
        max_idx = -1

        for i, num in enumerate(nums):
            if num > max_val:
                second_max = max_val
                max_val = num
                max_idx = i
            elif num > second_max:
                second_max = num

        return max_idx if max_val >= 2 * second_max else -1