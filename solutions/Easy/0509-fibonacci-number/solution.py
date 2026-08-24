# ──────────────────────────────────────────────────
# Problem  : 509. Fibonacci Number
# Difficulty: Easy
# Tags     : Math, Dynamic Programming, Recursion, Memoization
# Link     : https://leetcode.com/problems/fibonacci-number/
# Runtime  : 49 ms (beats 54%)
# Memory   : 19180000 (beats 58%)
# Language : python3
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
            
        return b