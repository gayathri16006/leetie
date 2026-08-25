# ──────────────────────────────────────────────────
# Problem  : 646. Maximum Length of Pair Chain
# Difficulty: Medium
# Tags     : Array, Dynamic Programming, Greedy, Sorting, Longest Increasing Subsequence
# Link     : https://leetcode.com/problems/maximum-length-of-pair-chain/
# Runtime  : 5 ms (beats 76%)
# Memory   : 19692000 (beats 34%)
# Language : python3
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

from typing import List

class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        # Sort pairs by their end values (right_i) in ascending order
        pairs.sort(key=lambda x: x[1])
        
        count = 0
        curr_end = float('-inf')
        
        for left, right in pairs:
            if left > curr_end:
                count += 1
                curr_end = right
                
        return count