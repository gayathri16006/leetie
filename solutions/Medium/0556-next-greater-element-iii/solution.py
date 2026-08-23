# ──────────────────────────────────────────────────
# Problem  : 556. Next Greater Element III
# Difficulty: Medium
# Tags     : Math, Two Pointers, String
# Link     : https://leetcode.com/problems/next-greater-element-iii/
# Runtime  : 0 ms (beats 100%)
# Memory   : 12208000 (beats 90%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def nextGreaterElement(self, n):
        digits = list(str(n))
        length = len(digits)
        
        # Step 1: Find the first decreasing element from the right
        i = length - 2
        while i >= 0 and digits[i] >= digits[i + 1]:
            i -= 1
            
        if i < 0:
            return -1
        
        # Step 2: Find the element just larger than digits[i] from the right
        j = length - 1
        while digits[j] <= digits[i]:
            j -= 1
            
        # Step 3: Swap digits[i] and digits[j]
        digits[i], digits[j] = digits[j], digits[i]
        
        # Step 4: Reverse the suffix from index i + 1 to the end
        digits[i + 1:] = reversed(digits[i + 1:])
        
        # Step 5: Convert back to integer and check 32-bit signed integer bounds
        res = int("".join(digits))
        return res if res <= (1 << 31) - 1 else -1