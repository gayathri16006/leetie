# ──────────────────────────────────────────────────
# Problem  : 504. Base 7
# Difficulty: Easy
# Tags     : Math, String
# Link     : https://leetcode.com/problems/base-7/
# Runtime  : 0 ms (beats 0%)
# Memory   : 19504000 (beats 0%)
# Language : python3
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        
        negative = num < 0
        num = abs(num)
        digits = []
        
        while num > 0:
            digits.append(str(num % 7))
            num //= 7
            
        if negative:
            digits.append("-")
            
        return "".join(reversed(digits))