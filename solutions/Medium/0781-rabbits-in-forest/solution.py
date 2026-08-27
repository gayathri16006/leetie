# ──────────────────────────────────────────────────
# Problem  : 781. Rabbits in Forest
# Difficulty: Medium
# Tags     : Array, Hash Table, Math, Greedy
# Link     : https://leetcode.com/problems/rabbits-in-forest/
# Runtime  : 0 ms (beats 100%)
# Memory   : 19424000 (beats 16%)
# Language : python3
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

from collections import Counter
import math

class Solution:
    def numRabbits(self, answers: list[int]) -> int:
        count = Counter(answers)
        total_rabbits = 0
        
        for ans, freq in count.items():
            group_size = ans + 1
            # Number of groups of this color needed: ceil(freq / group_size)
            groups = math.ceil(freq / group_size)
            total_rabbits += groups * group_size
            
        return total_rabbits