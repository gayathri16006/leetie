# ──────────────────────────────────────────────────
# Problem  : 784. Letter Case Permutation
# Difficulty: Medium
# Tags     : String, Backtracking, Bit Manipulation
# Link     : https://leetcode.com/problems/letter-case-permutation/
# Runtime  : 3 ms (beats 89%)
# Memory   : 19960000 (beats 82%)
# Language : python3
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def letterCasePermutation(self, s: str) -> list[str]:
        res = [""]
        
        for char in s:
            if char.isalpha():
                # Append both lowercase and uppercase variations
                res = [prefix + c for prefix in res for c in (char.lower(), char.upper())]
            else:
                # Keep digits and non-alphabetic characters as-is
                res = [prefix + char for prefix in res]
                
        return res