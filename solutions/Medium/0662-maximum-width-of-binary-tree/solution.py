# ──────────────────────────────────────────────────
# Problem  : 662. Maximum Width of Binary Tree
# Difficulty: Medium
# Tags     : Tree, Depth-First Search, Breadth-First Search, Binary Tree
# Link     : https://leetcode.com/problems/maximum-width-of-binary-tree/
# Runtime  : 8 ms (beats 6%)
# Memory   : 20240000 (beats 27%)
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
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        max_width = 0
        # Queue stores tuples of (node, index)
        queue = deque([(root, 0)])
        
        while queue:
            level_size = len(queue)
            # Normalize level indices using the leftmost node's index
            _, first_idx = queue[0]
            _, last_idx = queue[-1]
            
            max_width = max(max_width, last_idx - first_idx + 1)
            
            for _ in range(level_size):
                node, idx = queue.popleft()
                # Subtraction by first_idx prevents index values from growing excessively
                curr_idx = idx - first_idx
                
                if node.left:
                    queue.append((node.left, 2 * curr_idx))
                if node.right:
                    queue.append((node.right, 2 * curr_idx + 1))
                    
        return max_width