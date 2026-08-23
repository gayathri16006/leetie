# ──────────────────────────────────────────────────
# Problem  : 652. Find Duplicate Subtrees
# Difficulty: Medium
# Tags     : Hash Table, Tree, Depth-First Search, Binary Tree
# Link     : https://leetcode.com/problems/find-duplicate-subtrees/
# Runtime  : 11 ms (beats 26%)
# Memory   : 26828000 (beats 49%)
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

from collections import defaultdict
from typing import Optional, List

class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        counts = defaultdict(int)
        res = []
        
        def serialize(node):
            if not node:
                return "#"
            
            # Post-order serialization: root, left, right
            subtree = f"{node.val},{serialize(node.left)},{serialize(node.right)}"
            counts[subtree] += 1
            
            # Add to result only on the second encounter
            if counts[subtree] == 2:
                res.append(node)
                
            return subtree
        
        serialize(root)
        return res