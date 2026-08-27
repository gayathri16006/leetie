# ──────────────────────────────────────────────────
# Problem  : 738. Monotone Increasing Digits
# Difficulty: Medium
# Tags     : Math, Greedy
# Link     : https://leetcode.com/problems/monotone-increasing-digits/
# Runtime  : 0 ms (beats 0%)
# Memory   : 19204000 (beats 0%)
# Language : python3
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        digits = list(str(n))
        length = len(digits)
        mark = length  # Index from where all digits should become '9'
        
        # Traverse backwards to find the first violation of monotone increasing property
        for i in range(length - 1, 0, -1):
            if digits[i - 1] > digits[i]:
                digits[i - 1] = str(int(digits[i - 1]) - 1)
                mark = i
                
        # Fill all digits to the right with '9'
        for i in range(mark, length):
            digits[i] = '9'
            
        return int("".join(digits))