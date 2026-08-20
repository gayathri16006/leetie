# ──────────────────────────────────────────────────
# Problem  : 135. Candy
# Difficulty: Hard
# Tags     : Array, Greedy
# Link     : https://leetcode.com/problems/candy/
# Runtime  : 80 ms (beats 5%)
# Memory   : 17776000 (beats 8%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        n = len(ratings)
        candies = [1] * n
        
        # Left-to-right pass: satisfy condition for left neighbors
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1
                
        # Right-to-left pass: satisfy condition for right neighbors
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)
                
        return sum(candies)