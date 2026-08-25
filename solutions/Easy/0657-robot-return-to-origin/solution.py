# ──────────────────────────────────────────────────
# Problem  : 657. Robot Return to Origin
# Difficulty: Easy
# Tags     : String, Simulation
# Link     : https://leetcode.com/problems/robot-return-to-origin/
# Runtime  : 0 ms (beats 100%)
# Memory   : 19252000 (beats 56%)
# Language : python3
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        # A robot returns to origin iff 'U' == 'D' and 'L' == 'R'
        return moves.count('U') == moves.count('D') and moves.count('L') == moves.count('R')