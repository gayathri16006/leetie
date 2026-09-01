# ──────────────────────────────────────────────────
# Problem  : 606. Construct String from Binary Tree
# Difficulty: Medium
# Tags     : String, Tree, Depth-First Search, Binary Tree
# Link     : https://leetcode.com/problems/construct-string-from-binary-tree/
# Runtime  : 4 ms (beats 44%)
# Memory   : 20208000 (beats 97%)
# Language : python3
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        
        res = str(root.val)
        
        # Include left child if either left or right exists
        if root.left or root.right:
            res += f"({self.tree2str(root.left)})"
        
        # Include right child only if it exists
        if root.right:
            res += f"({self.tree2str(root.right)})"
            
        return res