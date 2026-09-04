# ──────────────────────────────────────────────────
# Problem  : 875. Koko Eating Bananas
# Difficulty: Medium
# Tags     : Array, Binary Search
# Link     : https://leetcode.com/problems/koko-eating-bananas/
# Runtime  : 167 ms (beats 48%)
# Memory   : 13608000 (beats 15%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        left, right = 1, max(piles)

        while left < right:
            mid = (left + right) // 2
            
            # Calculate total hours needed at speed mid
            hours_needed = sum((p + mid - 1) // mid for p in piles)
            
            if hours_needed <= h:
                right = mid
            else:
                left = mid + 1

        return left