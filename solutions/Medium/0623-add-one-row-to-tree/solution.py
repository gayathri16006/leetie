# ──────────────────────────────────────────────────
# Problem  : 623. Add One Row to Tree
# Difficulty: Medium
# Tags     : Tree, Depth-First Search, Breadth-First Search, Binary Tree
# Link     : https://leetcode.com/problems/add-one-row-to-tree/
# Runtime  : 4 ms (beats 35%)
# Memory   : 16976000 (beats 45%)
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
    def addOneRow(self, root, val, depth):
        # Special case: Insert a new root at depth 1
        if depth == 1:
            new_root = TreeNode(val)
            new_root.left = root
            return new_root
        
        # Helper DFS function to insert nodes at depth - 1
        def dfs(node, cur_depth):
            if not node:
                return
            
            if cur_depth == depth - 1:
                # Splice new left node
                new_left = TreeNode(val)
                new_left.left = node.left
                node.left = new_left
                
                # Splice new right node
                new_right = TreeNode(val)
                new_right.right = node.right
                node.right = new_right
                return
            
            dfs(node.left, cur_depth + 1)
            dfs(node.right, cur_depth + 1)
            
        dfs(root, 1)
        return root