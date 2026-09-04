# ──────────────────────────────────────────────────
# Problem  : 891. Sum of Subsequence Widths
# Difficulty: Hard
# Tags     : Array, Math, Sorting
# Link     : https://leetcode.com/problems/sum-of-subsequence-widths/
# Runtime  : 0 ms (beats 0%)
# Memory   : 12216000 (beats 0%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def sumSubseqWidths(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7
        nums.sort()
        n = len(nums)

        # Precompute powers of 2 modulo MOD
        pow2 = [1] * n
        for i in range(1, n):
            pow2[i] = (pow2[i - 1] * 2) % MOD

        total_width = 0
        for i in range(n):
            # nums[i] is max for 2^i subsequences, min for 2^(n - 1 - i) subsequences
            contrib = (pow2[i] - pow2[n - 1 - i]) * nums[i]
            total_width = (total_width + contrib) % MOD

        return total_width