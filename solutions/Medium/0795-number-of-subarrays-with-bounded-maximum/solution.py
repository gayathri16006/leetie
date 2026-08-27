# ──────────────────────────────────────────────────
# Problem  : 795. Number of Subarrays with Bounded Maximum
# Difficulty: Medium
# Tags     : Array, Two Pointers
# Link     : https://leetcode.com/problems/number-of-subarrays-with-bounded-maximum/
# Runtime  : 12 ms (beats 99%)
# Memory   : 25564000 (beats 80%)
# Language : python3
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def numSubarrayBoundedMax(self, nums: list[int], left: int, right: int) -> int:
        def count_subarrays_le(bound: int) -> int:
            """Counts subarrays where all elements are <= bound."""
            total = 0
            cur_len = 0
            for x in nums:
                if x <= bound:
                    cur_len += 1
                    total += cur_len
                else:
                    cur_len = 0
            return total

        # Subarrays with max in [left, right] = (max <= right) - (max <= left - 1)
        return count_subarrays_le(right) - count_subarrays_le(left - 1)