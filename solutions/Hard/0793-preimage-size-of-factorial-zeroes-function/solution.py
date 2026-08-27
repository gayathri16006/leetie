# ──────────────────────────────────────────────────
# Problem  : 793. Preimage Size of Factorial Zeroes Function
# Difficulty: Hard
# Tags     : Math, Binary Search
# Link     : https://leetcode.com/problems/preimage-size-of-factorial-zeroes-function/
# Runtime  : 0 ms (beats 0%)
# Memory   : 19340000 (beats 0%)
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

        # Binary search range: 0 to 5 * (k + 1)
        left, right = 0, 5 * (k + 1)
        while left <= right:
            mid = (left + right) // 2
            zeros = trailing_zeroes(mid)
            
            if zeros == k:
                # Any valid count corresponds to exactly 5 integers: {5m, 5m+1, 5m+2, 5m+3, 5m+4}
                return 5
            elif zeros < k:
                left = mid + 1
            else:
                right = mid - 1
                
        # If no integer has exactly k trailing zeroes
        return 0