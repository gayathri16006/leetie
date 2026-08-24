# ──────────────────────────────────────────────────
# Problem  : 605. Can Place Flowers
# Difficulty: Easy
# Tags     : Array, Greedy
# Link     : https://leetcode.com/problems/can-place-flowers/
# Runtime  : 0 ms (beats 0%)
# Memory   : 12340000 (beats 0%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        length = len(flowerbed)
        
        for i in range(length):
            if n <= 0:
                return True
            
            if flowerbed[i] == 0:
                prev_empty = (i == 0 or flowerbed[i - 1] == 0)
                next_empty = (i == length - 1 or flowerbed[i + 1] == 0)
                
                if prev_empty and next_empty:
                    flowerbed[i] = 1
                    n -= 1
                    
        return n <= 0