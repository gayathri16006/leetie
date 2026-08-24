# ──────────────────────────────────────────────────
# Problem  : 572. Subtree of Another Tree
# Difficulty: Easy
# Tags     : Tree, Depth-First Search, String Matching, Binary Tree, Hash Function
# Link     : https://leetcode.com/problems/subtree-of-another-tree/
# Runtime  : 0 ms (beats 0%)
# Memory   : 12324000 (beats 0%)
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
    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """
        def isSameTree(p, q):
            if not p and not q:
                return True
            if not p or not q or p.val != q.val:
                return False
            return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

        if not root:
            return False
        
        # Check if identical at current node, or search in left/right subtrees
        if isSameTree(root, subRoot):
            return True
            
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)