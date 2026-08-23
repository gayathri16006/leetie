# ──────────────────────────────────────────────────
# Problem  : 1927. Sum Game
# Difficulty: Medium
# Tags     : Math, String, Greedy, Game Theory
# Link     : https://leetcode.com/problems/sum-game/
# Runtime  : 36 ms (beats 96%)
# Memory   : 19880000 (beats 65%)
# Language : python3
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def sumGame(self, num: str) -> bool:
        n = len(num)
        half = n // 2
        
        sum1 = sum(int(c) for c in num[:half] if c != '?')
        cnt1 = num[:half].count('?')
        
        sum2 = sum(int(c) for c in num[half:] if c != '?')
        cnt2 = num[half:].count('?')
        
        # If Alice cannot be countered, or the expected balance is off, Alice wins.
        return 2 * (sum1 - sum2) != (cnt2 - cnt1) * 9