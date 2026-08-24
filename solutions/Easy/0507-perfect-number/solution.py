# ──────────────────────────────────────────────────
# Problem  : 507. Perfect Number
# Difficulty: Easy
# Tags     : Math
# Link     : https://leetcode.com/problems/perfect-number/
# Runtime  : 1 ms (beats 94%)
# Memory   : 19064000 (beats 98%)
# Language : python3
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        # Numbers <= 1 cannot be perfect numbers
        if num <= 1:
            return False
        
        divisors_sum = 1  # 1 is always a proper divisor for num > 1
        limit = int(num ** 0.5)
        
        for i in range(2, limit + 1):
            if num % i == 0:
                divisors_sum += i
                # Add the paired divisor if it is not the square root itself
                if i * i != num:
                    divisors_sum += num // i
                    
        return divisors_sum == num