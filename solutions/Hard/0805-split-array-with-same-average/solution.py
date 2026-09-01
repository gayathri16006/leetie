# ──────────────────────────────────────────────────
# Problem  : 805. Split Array With Same Average
# Difficulty: Hard
# Tags     : Array, Hash Table, Math, Dynamic Programming, Bit Manipulation, Meet in the Middle, Bitmask
# Link     : https://leetcode.com/problems/split-array-with-same-average/
# Runtime  : 1529 ms (beats 54%)
# Memory   : 53552000 (beats 54%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def splitArraySameAverage(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        if n == 1:
            return False
        
        total_sum = sum(nums)
        m = n // 2
        
        # Check if any subset size k from 1 to m can have an integer sum
        possible = any((total_sum * k) % n == 0 for k in range(1, m + 1))
        if not possible:
            return False
        
        # dp[k] stores all possible sums of subsets of size k
        dp = [set() for _ in range(m + 1)]
        dp[0].add(0)
        
        for num in nums:
            for k in range(m, 0, -1):
                for prev_sum in dp[k - 1]:
                    dp[k].add(prev_sum + num)
                    
        for k in range(1, m + 1):
            if (total_sum * k) % n == 0 and ((total_sum * k) // n) in dp[k]:
                return True
                
        return False