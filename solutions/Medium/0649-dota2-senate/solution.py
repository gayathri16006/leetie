# ──────────────────────────────────────────────────
# Problem  : 649. Dota2 Senate
# Difficulty: Medium
# Tags     : String, Greedy, Queue
# Link     : https://leetcode.com/problems/dota2-senate/
# Runtime  : 11 ms (beats 79%)
# Memory   : 19696000 (beats 38%)
# Language : python3
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        radiant = deque()
        dire = deque()
        n = len(senate)
        
        # Store the initial turn indices for each senator
        for i, char in enumerate(senate):
            if char == 'R':
                radiant.append(i)
            else:
                dire.append(i)
                
        # Simulate voting rounds
        while radiant and dire:
            r_idx = radiant.popleft()
            d_idx = dire.popleft()
            
            # The senator whose turn comes first bans the other senator
            # and gets re-queued for the next round (index offset by n)
            if r_idx < d_idx:
                radiant.append(r_idx + n)
            else:
                dire.append(d_idx + n)
                
        return "Radiant" if radiant else "Dire"