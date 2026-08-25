# ──────────────────────────────────────────────────
# Problem  : 670. Maximum Swap
# Difficulty: Medium
# Tags     : Math, Greedy
# Link     : https://leetcode.com/problems/maximum-swap/
# Runtime  : 4 ms (beats 1%)
# Memory   : 19220000 (beats 65%)
# Language : python3
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def maximumSwap(self, num: int) -> int:
        digits = list(str(num))
        
        # Record the last seen index for each digit (0-9)
        last = {int(d): i for i, d in enumerate(digits)}
        
        # Scan from left to right to find a digit that can be swapped with a larger digit appearing later
        for i, d in enumerate(digits):
            for larger_digit in range(9, int(d), -1):
                if larger_digit in last and last[larger_digit] > i:
                    # Swap the current digit with the last occurrence of the larger digit
                    swap_idx = last[larger_digit]
                    digits[i], digits[swap_idx] = digits[swap_idx], digits[i]
                    return int("".join(digits))
                    
        return num