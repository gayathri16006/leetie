# ──────────────────────────────────────────────────
# Problem  : 965. Univalued Binary Tree
# Difficulty: Easy
# Tags     : Tree, Depth-First Search, Breadth-First Search, Binary Tree
# Link     : https://leetcode.com/problems/univalued-binary-tree/
# Runtime  : 0 ms (beats 0%)
# Memory   : 12524000 (beats 0%)
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
    def isUnivalTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if not root:
            return True
        
        # Check left child value
        if root.left:
            if root.left.val != root.val or not self.isUnivalTree(root.left):
                return False
                
        # Check right child value
        if root.right:
            if root.right.val != root.val or not self.isUnivalTree(root.right):
                return False
                
        return True