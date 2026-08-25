# ──────────────────────────────────────────────────
# Problem  : 669. Trim a Binary Search Tree
# Difficulty: Medium
# Tags     : Tree, Depth-First Search, Binary Search Tree, Binary Tree
# Link     : https://leetcode.com/problems/trim-a-binary-search-tree/
# Runtime  : 0 ms (beats 0%)
# Memory   : 19072000 (beats 0%)
# Language : python3
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        # If current node's value is less than low, the left subtree is also out of bounds
        if root.val < low:
            return self.trimBST(root.right, low, high)
        
        # If current node's value is greater than high, the right subtree is also out of bounds
        if root.val > high:
            return self.trimBST(root.left, low, high)
        
        # If root value is within [low, high], recursively trim both subtrees
        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)
        
        return root