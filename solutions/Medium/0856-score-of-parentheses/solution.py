# ──────────────────────────────────────────────────
# Problem  : 856. Score of Parentheses
# Difficulty: Medium
# Tags     : String, Stack, Bracket Sequences
# Link     : https://leetcode.com/problems/score-of-parentheses/
# Runtime  : 0 ms (beats 0%)
# Memory   : 12444000 (beats 0%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def scoreOfParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        depth = 0

        for i, ch in enumerate(s):
            if ch == '(':
                depth += 1
            else:
                depth -= 1
                # If this ')' immediately closes an '(', it is an innermost pair
                if s[i - 1] == '(':
                    ans += 1 << depth

        return ans