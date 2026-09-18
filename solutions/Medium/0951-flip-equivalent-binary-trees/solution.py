# ──────────────────────────────────────────────────
# Problem  : 951. Flip Equivalent Binary Trees
# Difficulty: Medium
# Tags     : Tree, Depth-First Search, Binary Tree
# Link     : https://leetcode.com/problems/flip-equivalent-binary-trees/
# Runtime  : 0 ms (beats 100%)
# Memory   : 12552000 (beats 28%)
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
    def flipEquiv(self, root1, root2):
        """
        :type root1: Optional[TreeNode]
        :type root2: Optional[TreeNode]
        :rtype: bool
        """
        # Both null -> equivalent
        if not root1 and not root2:
            return True
        
        
        if not root1 or not root2 or root1.val != root2.val:
            return False
        
        
        no_flip = self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right)
        flip = self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left)
        
        return no_flip or flip