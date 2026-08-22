# ──────────────────────────────────────────────────
# Problem  : 114. Flatten Binary Tree to Linked List
# Difficulty: Medium
# Tags     : Linked List, Stack, Tree, Depth-First Search, Binary Tree
# Link     : https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
# Runtime  : 0 ms (beats 100%)
# Memory   : 19592000 (beats 41%)
# Language : python3
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        curr = root
        
        while curr:
            if curr.left:
                # Find the rightmost node in the left subtree
                prev = curr.left
                while prev.right:
                    prev = prev.right
                
                # Rewire connections
                prev.right = curr.right
                curr.right = curr.left
                curr.left = None
            
            # Move to the next node on the right
            curr = curr.right