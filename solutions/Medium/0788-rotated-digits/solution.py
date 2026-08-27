# ──────────────────────────────────────────────────
# Problem  : 788. Rotated Digits
# Difficulty: Medium
# Tags     : Math, Dynamic Programming
# Link     : https://leetcode.com/problems/rotated-digits/
# Runtime  : 59 ms (beats 14%)
# Memory   : 19160000 (beats 91%)
# Language : python3
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def rotatedDigits(self, n: int) -> int:
        # Invalid digits that become invalid numbers when rotated
        invalid = {'3', '4', '7'}
        # Digits that rotate to a different valid digit (must have at least one)
        diff = {'2', '5', '6', '9'}
        
        count = 0
        for i in range(1, n + 1):
            s = str(i)
            # Must not contain 3, 4, or 7, and must contain at least one of 2, 5, 6, 9
            if not any(c in invalid for c in s) and any(c in diff for c in s):
                count += 1
                
        return count