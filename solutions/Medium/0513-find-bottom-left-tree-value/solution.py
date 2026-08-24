# ──────────────────────────────────────────────────
# Problem  : 513. Find Bottom Left Tree Value
# Difficulty: Medium
# Tags     : Tree, Depth-First Search, Breadth-First Search, Binary Tree
# Link     : https://leetcode.com/problems/find-bottom-left-tree-value/
# Runtime  : 0 ms (beats 0%)
# Memory   : 19188000 (beats 0%)
# Language : python3
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

from collections import deque
from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        node = root
        
        while queue:
            node = queue.popleft()
            
            # Add right child first, then left child
            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)
                
        return node.val