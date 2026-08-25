# ──────────────────────────────────────────────────
# Problem  : 687. Longest Univalue Path
# Difficulty: Medium
# Tags     : Tree, Depth-First Search, Binary Tree, DP on Trees
# Link     : https://leetcode.com/problems/longest-univalue-path/
# Runtime  : 36 ms (beats 74%)
# Memory   : 21920000 (beats 96%)
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
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        max_len = 0
        
        def dfs(node: Optional[TreeNode]) -> int:
            nonlocal max_len
            if not node:
                return 0
            
            # Post-order DFS traversal
            left_len = dfs(node.left)
            right_len = dfs(node.right)
            
            left_arrow = 0
            right_arrow = 0
            
            # Check if left child continues the same value sequence
            if node.left and node.left.val == node.val:
                left_arrow = left_len + 1
                
            # Check if right child continues the same value sequence
            if node.right and node.right.val == node.val:
                right_arrow = right_len + 1
                
            # Update the longest path passing through the current node as an apex
            max_len = max(max_len, left_arrow + right_arrow)
            
            # Return single longest continuous branch to the parent
            return max(left_arrow, right_arrow)
            
        dfs(root)
        return max_len