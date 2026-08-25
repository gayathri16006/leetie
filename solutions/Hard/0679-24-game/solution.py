# ──────────────────────────────────────────────────
# Problem  : 679. 24 Game
# Difficulty: Hard
# Tags     : Array, Math, Backtracking
# Link     : https://leetcode.com/problems/24-game/
# Runtime  : 3 ms (beats 0%)
# Memory   : 19300000 (beats 0%)
# Language : python3
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

from typing import List

class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        EPSILON = 1e-6
        
        def solve(nums: List[float]) -> bool:
            if len(nums) == 1:
                return abs(nums[0] - 24) < EPSILON
            
            n = len(nums)
            for i in range(n):
                for j in range(n):
                    if i != j:
                        # Pick two distinct numbers and compute all valid results
                        next_nums = [nums[k] for k in range(n) if k != i and k != j]
                        
                        a, b = nums[i], nums[j]
                        candidates = [a + b, a - b, a * b]
                        if abs(b) > EPSILON:
                            candidates.append(a / b)
                            
                        for val in candidates:
                            next_nums.append(val)
                            if solve(next_nums):
                                return True
                            next_nums.pop()
                            
            return False

        return solve([float(x) for x in cards])