# ──────────────────────────────────────────────────
# Problem  : 682. Baseball Game
# Difficulty: Easy
# Tags     : Array, Stack, Simulation
# Link     : https://leetcode.com/problems/baseball-game/
# Runtime  : 0 ms (beats 0%)
# Memory   : 19224000 (beats 0%)
# Language : python3
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

from typing import List

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        
        for op in operations:
            if op == '+':
                record.append(record[-1] + record[-2])
            elif op == 'D':
                record.append(record[-1] * 2)
            elif op == 'C':
                record.pop()
            else:
                record.append(int(op))
                
        return sum(record)