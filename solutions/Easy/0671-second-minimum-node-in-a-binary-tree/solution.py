# ──────────────────────────────────────────────────
# Problem  : 671. Second Minimum Node In a Binary Tree
# Difficulty: Easy
# Tags     : Tree, Depth-First Search, Binary Tree
# Link     : https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/
# Runtime  : 0 ms (beats 100%)
# Memory   : 19432000 (beats 8%)
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
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        if not root or not root.left:
            return -1
        
        # If a child's value is different from root.val, it is candidate for min in that subtree
        left = root.left.val if root.left.val != root.val else self.findSecondMinimumValue(root.left)
        right = root.right.val if root.right.val != root.val else self.findSecondMinimumValue(root.right)
        
        # If both subtrees provide valid candidates, return the smaller one
        if left != -1 and right != -1:
            return min(left, right)
        
        # Otherwise, return the one that is valid (or -1 if neither is)
        return max(left, right)