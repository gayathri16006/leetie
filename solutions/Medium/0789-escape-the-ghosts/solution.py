# ──────────────────────────────────────────────────
# Problem  : 789. Escape The Ghosts
# Difficulty: Medium
# Tags     : Array, Math
# Link     : https://leetcode.com/problems/escape-the-ghosts/
# Runtime  : 0 ms (beats 100%)
# Memory   : 19292000 (beats 70%)
# Language : python3
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def escapeGhosts(self, ghosts: list[list[int]], target: list[int]) -> bool:
        tx, ty = target
        # Calculate the player's Manhattan distance to the target from (0, 0)
        player_dist = abs(tx) + abs(ty)
        
        # If any ghost can reach the target in <= steps, escape is impossible
        for gx, gy in ghosts:
            ghost_dist = abs(gx - tx) + abs(gy - ty)
            if ghost_dist <= player_dist:
                return False
                
        return True