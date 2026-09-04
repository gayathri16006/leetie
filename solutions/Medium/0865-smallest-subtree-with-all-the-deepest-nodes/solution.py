# ──────────────────────────────────────────────────
# Problem  : 865. Smallest Subtree with all the Deepest Nodes
# Difficulty: Medium
# Tags     : Hash Table, Tree, Depth-First Search, Breadth-First Search, Binary Tree, Binary Lifting, Lowest Common Ancestor, DP on Trees
# Link     : https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/
# Runtime  : 0 ms (beats 100%)
# Memory   : 12600000 (beats 96%)
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
    def subtreeWithAllDeepest(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        def dfs(node):
            if not node:
                return 0, None

            left_depth, left_node = dfs(node.left)
            right_depth, right_node = dfs(node.right)

            if left_depth == right_depth:
                return left_depth + 1, node
            elif left_depth > right_depth:
                return left_depth + 1, left_node
            else:
                return right_depth + 1, right_node

        return dfs(root)[1]