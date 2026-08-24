# ──────────────────────────────────────────────────
# Problem  : 514. Freedom Trail
# Difficulty: Hard
# Tags     : String, Dynamic Programming, Depth-First Search, Breadth-First Search
# Link     : https://leetcode.com/problems/freedom-trail/
# Runtime  : 55 ms (beats 81%)
# Memory   : 26460000 (beats 42%)
# Language : python3
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

from collections import defaultdict
from functools import lru_cache

class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        n = len(ring)
        
        # Store all indices for each character in the ring
        char_indices = defaultdict(list)
        for i, char in enumerate(ring):
            char_indices[char].append(i)
            
        @lru_cache(None)
        def dp(key_idx: int, ring_idx: int) -> int:
            # Base case: all characters in key are spelled
            if key_idx == len(key):
                return 0
            
            target_char = key[key_idx]
            min_steps = float('inf')
            
            # Try rotating to each occurrence of target_char
            for next_idx in char_indices[target_char]:
                # Minimum distance clockwise or counter-clockwise
                dist = abs(ring_idx - next_idx)
                rotations = min(dist, n - dist)
                
                # 1 extra step for pressing the center button
                total_cost = rotations + 1 + dp(key_idx + 1, next_idx)
                min_steps = min(min_steps, total_cost)
                
            return min_steps

        # Start at index 0 of key with ring aligned at index 0
        return dp(0, 0)