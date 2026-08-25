# ──────────────────────────────────────────────────
# Problem  : 667. Beautiful Arrangement II
# Difficulty: Medium
# Tags     : Array, Math
# Link     : https://leetcode.com/problems/beautiful-arrangement-ii/
# Runtime  : 0 ms (beats 0%)
# Memory   : 19284000 (beats 0%)
# Language : python3
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

from typing import List

class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        res = []
        left = 1
        right = k + 1
        
        # Alternate between left and right pointers to generate k distinct differences: k, k-1, ..., 1
        for i in range(k + 1):
            if i % 2 == 0:
                res.append(left)
                left += 1
            else:
                res.append(right)
                right -= 1
                
        # Append remaining elements in increasing order (producing difference 1)
        for val in range(k + 2, n + 1):
            res.append(val)
            
        return res