# ──────────────────────────────────────────────────
# Problem  : 441. Arranging Coins
# Difficulty: Easy
# Tags     : Math, Binary Search
# Link     : https://leetcode.com/problems/arranging-coins/
# Runtime  : 3 ms (beats 67%)
# Memory   : 12448000 (beats 18%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 0, n
        
        while left <= right:
            mid = left + (right - left) // 2
            coins_needed = mid * (mid + 1) // 2
            
            if coins_needed == n:
                return mid
            elif coins_needed < n:
                left = mid + 1
            else:
                right = mid - 1
                
        return right