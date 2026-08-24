# ──────────────────────────────────────────────────
# Problem  : 589. N-ary Tree Preorder Traversal
# Difficulty: Easy
# Tags     : Stack, Tree, Depth-First Search
# Link     : https://leetcode.com/problems/n-ary-tree-preorder-traversal/
# Runtime  : 35 ms (beats 58%)
# Memory   : 15428000 (beats 57%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        result = []

        def dfs(node):
            if not node:
                return
            result.append(node.val)
            for child in node.children:
                dfs(child)

        dfs(root)
        return result