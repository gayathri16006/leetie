# ──────────────────────────────────────────────────
# Problem  : 780. Reaching Points
# Difficulty: Hard
# Tags     : Math, Euclidean Algorithm, Greatest Common Divisor
# Link     : https://leetcode.com/problems/reaching-points/
# Runtime  : 0 ms (beats 100%)
# Memory   : 19336000 (beats 41%)
# Language : python3
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        # Work backwards from (tx, ty) to (sx, sy) using modulo arithmetic
        while tx >= sx and ty >= sy:
            if tx == sx and ty == sy:
                return True
            
            if tx > ty:
                if ty > sy:
                    tx %= ty
                else:
                    # When ty == sy, we can only decrease tx by multiples of ty (which is sy)
                    return (tx - sx) % ty == 0
            else:
                if tx > sx:
                    ty %= tx
                else:
                    # When tx == sx, we can only decrease ty by multiples of tx (which is sx)
                    return (ty - sy) % tx == 0
                    
        return False