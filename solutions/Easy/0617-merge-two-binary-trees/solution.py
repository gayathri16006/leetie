# ──────────────────────────────────────────────────
# Problem  : 617. Merge Two Binary Trees
# Difficulty: Easy
# Tags     : Tree, Depth-First Search, Breadth-First Search, Binary Tree
# Link     : https://leetcode.com/problems/merge-two-binary-trees/
# Runtime  : 1 ms (beats 76%)
# Memory   : 13072000 (beats 78%)
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
    def mergeTrees(self, root1, root2):
        # If one of the nodes is None, return the other
        if not root1:
            return root2
        if not root2:
            return root1
        
        # Merge current node values into root1 (in-place)
        root1.val += root2.val
        
        # Recursively merge left and right subtrees
        root1.left = self.mergeTrees(root1.left, root2.left)
        root1.right = self.mergeTrees(root1.right, root2.right)
        
        return root1