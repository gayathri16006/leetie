# ──────────────────────────────────────────────────
# Problem  : 938. Range Sum of BST
# Difficulty: Easy
# Tags     : Tree, Depth-First Search, Binary Search Tree, Binary Tree
# Link     : https://leetcode.com/problems/range-sum-of-bst/
# Runtime  : 1 ms (beats 98%)
# Memory   : 28760000 (beats 48%)
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
    def rangeSumBST(self, root, low, high):
        """
        :type root: Optional[TreeNode]
        :type low: int
        :type high: int
        :rtype: int
        """
        if not root:
            return 0
        
        # If current value is greater than high, skip the right subtree
        if root.val > high:
            return self.rangeSumBST(root.left, low, high)
        
        # If current value is less than low, skip the left subtree
        if root.val < low:
            return self.rangeSumBST(root.right, low, high)
        
        # Current value is within [low, high]
        return root.val + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)