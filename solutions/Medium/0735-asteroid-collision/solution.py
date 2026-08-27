# ──────────────────────────────────────────────────
# Problem  : 735. Asteroid Collision
# Difficulty: Medium
# Tags     : Array, Stack, Simulation
# Link     : https://leetcode.com/problems/asteroid-collision/
# Runtime  : 0 ms (beats 100%)
# Memory   : 20232000 (beats 71%)
# Language : python3
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack = []
        
        for ast in asteroids:
            # A collision only occurs if the current asteroid moves left (< 0) 
            # and the previous asteroid on the stack moves right (> 0)
            while stack and ast < 0 < stack[-1]:
                if stack[-1] < -ast:
                    # Previous smaller right-moving asteroid explodes
                    stack.pop()
                    continue
                elif stack[-1] == -ast:
                    # Both asteroids are equal size and destroy each other
                    stack.pop()
                break
            else:
                # No collision occurred or the incoming asteroid survived all collisions
                stack.append(ast)
                
        return stack