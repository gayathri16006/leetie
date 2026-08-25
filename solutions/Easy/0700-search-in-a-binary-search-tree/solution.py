# ──────────────────────────────────────────────────
# Problem  : 700. Search in a Binary Search Tree
# Difficulty: Easy
# Tags     : Tree, Binary Search Tree, Binary Tree
# Link     : https://leetcode.com/problems/search-in-a-binary-search-tree/
# Runtime  : 0 ms (beats 100%)
# Memory   : 20940000 (beats 40%)
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
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        curr = root
        
        while curr:
            if curr.val == val:
                return curr
            elif val < curr.val:
                curr = curr.left
            else:
                curr = curr.right
                
        return None