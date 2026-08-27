# ──────────────────────────────────────────────────
# Problem  : 793. Preimage Size of Factorial Zeroes Function
# Difficulty: Hard
# Tags     : Math, Binary Search
# Link     : https://leetcode.com/problems/preimage-size-of-factorial-zeroes-function/
# Runtime  : 1 ms (beats 30%)
# Memory   : 19460000 (beats 16%)
# Language : python3
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def preimageSizeFZF(self, k: int) -> int:
        def trailing_zeroes(x: int) -> int:
            count = 0
            while x > 0:
                count += x // 5
                x //= 5
            return count

        # Binary search for any x where trailing_zeroes(x) == k
        left, right = 0, 5 * (k + 1)
        while left <= right:
            mid = (left + right) // 2
            zeros = trailing_zeroes(mid)
            
            if zeros == k:
                # If any x has exactly k trailing zeroes, there are always exactly 5 consecutive numbers
                return 5
            elif zeros < k:
                left = mid + 1
            else:
                right = mid - 1
                
        # If no such x exists, the preimage size is 0
        return 0