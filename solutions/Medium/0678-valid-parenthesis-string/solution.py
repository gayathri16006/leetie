# ──────────────────────────────────────────────────
# Problem  : 678. Valid Parenthesis String
# Difficulty: Medium
# Tags     : String, Dynamic Programming, Stack, Greedy, Bracket Sequences
# Link     : https://leetcode.com/problems/valid-parenthesis-string/
# Runtime  : 0 ms (beats 0%)
# Memory   : 19224000 (beats 0%)
# Language : python3
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def checkValidString(self, s: str) -> bool:
        # cmin: minimum possible number of open '(' brackets
        # cmax: maximum possible number of open '(' brackets
        cmin = cmax = 0
        
        for ch in s:
            if ch == '(':
                cmin += 1
                cmax += 1
            elif ch == ')':
                cmin -= 1
                cmax -= 1
            else:  # ch == '*'
                cmin -= 1  # treat '*' as ')'
                cmax += 1  # treat '*' as '('
                # treating '*' as '' leaves counts unchanged
            
            # Too many ')' even if all '*' were treated as '('
            if cmax < 0:
                return False
            
            # cmin cannot be negative (we can't have negative unmatched open brackets)
            cmin = max(cmin, 0)
            
        return cmin == 0