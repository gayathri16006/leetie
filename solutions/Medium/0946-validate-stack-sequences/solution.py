# ──────────────────────────────────────────────────
# Problem  : 946. Validate Stack Sequences
# Difficulty: Medium
# Tags     : Array, Stack, Simulation
# Link     : https://leetcode.com/problems/validate-stack-sequences/
# Runtime  : 2 ms (beats 65%)
# Memory   : 12412000 (beats 68%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        stack = []
        j = 0
        
        for val in pushed:
            stack.append(val)
            while stack and stack[-1] == popped[j]:
                stack.pop()
                j += 1
                
        return not stack