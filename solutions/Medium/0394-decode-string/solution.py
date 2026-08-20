# ──────────────────────────────────────────────────
# Problem  : 394. Decode String
# Difficulty: Medium
# Tags     : String, Stack, Recursion
# Link     : https://leetcode.com/problems/decode-string/
# Runtime  : 0 ms (beats 100%)
# Memory   : 12304000 (beats 57%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        curr_str = ""
        curr_num = 0

        for ch in s:
            if ch.isdigit():
                curr_num = curr_num * 10 + int(ch)
            elif ch == '[':
                # Push the previous string and current multiplier onto the stack
                stack.append((curr_str, curr_num))
                # Reset for the new inner expression
                curr_str = ""
                curr_num = 0
            elif ch == ']':
                # Pop previous context and repeat current string
                prev_str, repeat_k = stack.pop()
                curr_str = prev_str + curr_str * repeat_k
            else:
                curr_str += ch

        return curr_str