# ──────────────────────────────────────────────────
# Problem  : 739. Daily Temperatures
# Difficulty: Medium
# Tags     : Array, Stack, Monotonic Stack
# Link     : https://leetcode.com/problems/daily-temperatures/
# Runtime  : 125 ms (beats 16%)
# Memory   : 35924000 (beats 7%)
# Language : python3
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        res = [0] * len(temperatures)
        stack = []  # stores pairs of [temperature, index]

        for i, t in enumerate(temperatures):
            # Resolve all previous colder days when a warmer day is encountered
            while stack and t > stack[-1][0]:
                prev_t, prev_i = stack.pop()
                res[prev_i] = i - prev_i
            stack.append([t, i])

        return res