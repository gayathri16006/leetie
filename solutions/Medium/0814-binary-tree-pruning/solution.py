# ──────────────────────────────────────────────────
# Problem  : 814. Binary Tree Pruning
# Difficulty: Medium
# Tags     : Tree, Depth-First Search, Binary Tree
# Link     : https://leetcode.com/problems/binary-tree-pruning/
# Runtime  : 0 ms (beats 0%)
# Memory   : 12292000 (beats 0%)
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
    def pruneTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        if not root:
            return None
        
        # Recursively prune left and right subtrees
        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)
        
        # If the node's value is 0 and both children are pruned (None), remove this node
        if root.val == 0 and not root.left and not root.right:
            return None
            
        return root