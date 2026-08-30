# ──────────────────────────────────────────────────
# Problem  : 2091. Removing Minimum and Maximum From Array
# Difficulty: Medium
# Tags     : Array, Greedy
# Link     : https://leetcode.com/problems/removing-minimum-and-maximum-from-array/
# Runtime  : 15 ms (beats 81%)
# Memory   : 33640000 (beats 35%)
# Language : python3
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        mn = nums.index(min(nums))
        mx = nums.index(max(nums))

        a = min(mn, mx)
        b = max(mn, mx)

        return min(
            b + 1,          # remove both from front
            n - a,          # remove both from back
            (a + 1) + (n - b)  # min from front, max from back
        )