# ──────────────────────────────────────────────────
# Problem  : 517. Super Washing Machines
# Difficulty: Hard
# Tags     : Array, Greedy
# Link     : https://leetcode.com/problems/super-washing-machines/
# Runtime  : 7 ms (beats 15%)
# Memory   : 20036000 (beats 62%)
# Language : python3
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def findMinMoves(self, machines: list[int]) -> int:
        total = sum(machines)
        n = len(machines)
        
        # If dresses cannot be distributed equally
        if total % n != 0:
            return -1
        
        target = total // n
        max_moves = 0
        running_sum = 0
        
        for load in machines:
            diff = load - target
            running_sum += diff
            # The bottleneck is the max of:
            # 1. Total flow passing through this split point (|running_sum|)
            # 2. Total dresses this machine needs to give away (diff)
            max_moves = max(max_moves, abs(running_sum), diff)
            
        return max_moves