# ──────────────────────────────────────────────────
# Problem  : 650. 2 Keys Keyboard
# Difficulty: Medium
# Tags     : Math, Dynamic Programming
# Link     : https://leetcode.com/problems/2-keys-keyboard/
# Runtime  : 0 ms (beats 0%)
# Memory   : 19324000 (beats 0%)
# Language : python3
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def minSteps(self, n: int) -> int:
        steps = 0
        factor = 2
        
        # Prime factorization: the minimum operations equal the sum of prime factors
        while n > 1:
            while n % factor == 0:
                steps += factor
                n //= factor
            factor += 1
            
        return steps