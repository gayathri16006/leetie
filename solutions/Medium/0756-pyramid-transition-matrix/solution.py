# ──────────────────────────────────────────────────
# Problem  : 756. Pyramid Transition Matrix
# Difficulty: Medium
# Tags     : Hash Table, String, Backtracking, Bit Manipulation
# Link     : https://leetcode.com/problems/pyramid-transition-matrix/
# Runtime  : 0 ms (beats 0%)
# Memory   : 19216000 (beats 0%)
# Language : python3
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

from collections import defaultdict
import itertools

class Solution:
    def pyramidTransition(self, bottom: str, allowed: list[str]) -> bool:
        # Build mapping: (left_block, right_block) -> [valid_top_blocks]
        transitions = defaultdict(list)
        for pattern in allowed:
            transitions[(pattern[0], pattern[1])].append(pattern[2])
            
        memo = {}

        def can_build(current_row: str) -> bool:
            if len(current_row) == 1:
                return True
            if current_row in memo:
                return memo[current_row]
            
            # Generate valid possibilities for each adjacent pair
            options = []
            for i in range(len(current_row) - 1):
                pair = (current_row[i], current_row[i + 1])
                if pair not in transitions:
                    memo[current_row] = False
                    return False
                options.append(transitions[pair])
            
            # Try all candidate next rows using Cartesian product
            for next_row in itertools.product(*options):
                if can_build("".join(next_row)):
                    memo[current_row] = True
                    return True
                    
            memo[current_row] = False
            return False

        return can_build(bottom)