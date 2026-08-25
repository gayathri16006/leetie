# ──────────────────────────────────────────────────
# Problem  : 653. Two Sum IV - Input is a BST
# Difficulty: Easy
# Tags     : Hash Table, Two Pointers, Tree, Depth-First Search, Breadth-First Search, Binary Search Tree, Binary Tree
# Link     : https://leetcode.com/problems/two-sum-iv-input-is-a-bst/
# Runtime  : 0 ms (beats 0%)
# Memory   : 19200000 (beats 0%)
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
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        seen = set()
        
        def dfs(node: Optional[TreeNode]) -> bool:
            if not node:
                return False
            
            # Check if complement exists
            if (k - node.val) in seen:
                return True
            
            seen.add(node.val)
            
            return dfs(node.left) or dfs(node.right)
            
        return dfs(root)