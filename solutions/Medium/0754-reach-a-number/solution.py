# ──────────────────────────────────────────────────
# Problem  : 754. Reach a Number
# Difficulty: Medium
# Tags     : Math, Binary Search
# Link     : https://leetcode.com/problems/reach-a-number/
# Runtime  : 39 ms (beats 62%)
# Memory   : 19224000 (beats 53%)
# Language : python3
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        k = 0
        current_sum = 0
        
        while current_sum < target or (current_sum - target) % 2 != 0:
            k += 1
            current_sum += k
            
        return k