# ──────────────────────────────────────────────────
# Problem  : 672. Bulb Switcher II
# Difficulty: Medium
# Tags     : Math, Bit Manipulation, Depth-First Search, Breadth-First Search
# Link     : https://leetcode.com/problems/bulb-switcher-ii/
# Runtime  : 0 ms (beats 100%)
# Memory   : 19392000 (beats 33%)
# Language : python3
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def flipLights(self, n: int, presses: int) -> int:
        if presses == 0:
            return 1
        if n == 1:
            return 2
        if n == 2:
            return 3 if presses == 1 else 4
        
        # For n >= 3
        if presses == 1:
            return 4
        if presses == 2:
            return 7
        return 8