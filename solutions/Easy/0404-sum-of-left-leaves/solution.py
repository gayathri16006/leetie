# ──────────────────────────────────────────────────
# Problem  : 404. Sum of Left Leaves
# Difficulty: Easy
# Tags     : Tree, Depth-First Search, Breadth-First Search, Binary Tree
# Link     : https://leetcode.com/problems/sum-of-left-leaves/
# Runtime  : 0 ms (beats 100%)
# Memory   : 13236000 (beats 23%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def dfs(node, is_left):
            if not node:
                return 0
            
            # Check if it's a leaf node
            if not node.left and not node.right:
                return node.val if is_left else 0
            
            # Recurse left with is_left=True, right with is_left=False
            return dfs(node.left, True) + dfs(node.right, False)
            
        return dfs(root, False)