# ──────────────────────────────────────────────────
# Problem  : 668. Kth Smallest Number in Multiplication Table
# Difficulty: Hard
# Tags     : Math, Binary Search
# Link     : https://leetcode.com/problems/kth-smallest-number-in-multiplication-table/
# Runtime  : 323 ms (beats 40%)
# Memory   : 19224000 (beats 70%)
# Language : python3
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        def count_less_equal(x: int) -> int:
            # Count elements in the m x n table <= x
            count = 0
            for i in range(1, m + 1):
                count += min(x // i, n)
            return count

        left, right = 1, m * n
        
        while left < right:
            mid = (left + right) // 2
            
            if count_less_equal(mid) >= k:
                right = mid
            else:
                left = mid + 1
                
        return left