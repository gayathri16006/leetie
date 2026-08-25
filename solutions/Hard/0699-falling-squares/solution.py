# ──────────────────────────────────────────────────
# Problem  : 699. Falling Squares
# Difficulty: Hard
# Tags     : Array, Segment Tree, Ordered Set
# Link     : https://leetcode.com/problems/falling-squares/
# Runtime  : 318 ms (beats 14%)
# Memory   : 19660000 (beats 90%)
# Language : python3
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

from typing import List

class Solution:
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        # intervals will store tuples of (left, right, top_height)
        intervals = []
        ans = []
        max_height = 0
        
        for left, size in positions:
            right = left + size
            base_height = 0
            
            # Check overlap with all previously placed squares
            for l, r, h in intervals:
                # Two intervals [left, right) and [l, r) overlap if max(left, l) < min(right, r)
                if max(left, l) < min(right, r):
                    base_height = max(base_height, h)
                    
            top_height = base_height + size
            intervals.append((left, right, top_height))
            
            max_height = max(max_height, top_height)
            ans.append(max_height)
            
        return ans