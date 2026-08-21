# ──────────────────────────────────────────────────
# Problem  : 385. Mini Parser
# Difficulty: Medium
# Tags     : String, Stack, Depth-First Search
# Link     : https://leetcode.com/problems/mini-parser/
# Runtime  : 0 ms (beats 0%)
# Memory   : 12396000 (beats 0%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger(object):
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested element elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution(object):
    def deserialize(self, s):
        """
        :type s: str
        :rtype: NestedInteger
        """
        # If the input contains only a single integer
        if not s.startswith('['):
            return NestedInteger(int(s))
        
        stack = []
        num_str = ""
        
        for char in s:
            if char == '[':
                # Start a new nested list and push to stack
                new_list = NestedInteger()
                stack.append(new_list)
            elif char in ',]':
                # If there's an accumulated integer, add it to the current list
                if num_str:
                    stack[-1].add(NestedInteger(int(num_str)))
                    num_str = ""
                # If closing bracket, pop current list and add it to its parent list
                if char == ']' and len(stack) > 1:
                    completed_list = stack.pop()
                    stack[-1].add(completed_list)
            else:
                # Accumulate digits and negative signs
                num_str += char
                
        return stack[0]