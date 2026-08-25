# ──────────────────────────────────────────────────
# Problem  : 652. Find Duplicate Subtrees
# Difficulty: Medium
# Tags     : Hash Table, Tree, Depth-First Search, Binary Tree
# Link     : https://leetcode.com/problems/find-duplicate-subtrees/
# Runtime  : 4 ms (beats 73%)
# Memory   : 26856000 (beats 49%)
# Language : python3
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

from collections import defaultdict
from typing import Optional, List

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        subtrees = defaultdict(int)
        duplicates = []
        
        def serialize(node: Optional[TreeNode]) -> str:
            if not node:
                return "#"
            
            # Post-order traversal representation: root,left,right
            serial = f"{node.val},{serialize(node.left)},{serialize(node.right)}"
            subtrees[serial] += 1
            
            # Only append the first time a duplicate is detected
            if subtrees[serial] == 2:
                duplicates.append(node)
                
            return serial
            
        serialize(root)
        return duplicates