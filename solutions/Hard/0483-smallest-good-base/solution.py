# ──────────────────────────────────────────────────
# Problem  : 483. Smallest Good Base
# Difficulty: Hard
# Tags     : Math, Binary Search
# Link     : https://leetcode.com/problems/smallest-good-base/
# Runtime  : 4 ms (beats 84%)
# Memory   : 12308000 (beats 56%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

import math

class Solution(object):
    def smallestGoodBase(self, n):
        """
        :type n: str
        :rtype: str
        """
        num = int(n)
        # The maximum number of digits (all 1s in base 2) is log2(num) + 1
        max_m = int(math.log(num, 2)) + 1

        for m in range(max_m, 2, -1):
            # Estimate base k: since num ≈ k^(m-1), k ≈ num^(1/(m-1))
            k = int(num ** (1.0 / (m - 1)))
            
            if k >= 2:
                # Check if 1 + k + k^2 + ... + k^(m-1) == num
                # Using geometric sum formula: (k^m - 1) // (k - 1)
                total = 0
                cur = 1
                for _ in range(m):
                    total += cur
                    cur *= k
                
                if total == num:
                    return str(k)

        # Fallback: for m = 2, n = 1 + k => k = n - 1
        return str(num - 1)