# ──────────────────────────────────────────────────
# Problem  : 530. Minimum Absolute Difference in BST
# Difficulty: Easy
# Tags     : Tree, Depth-First Search, Breadth-First Search, Binary Search Tree, Binary Tree
# Link     : https://leetcode.com/problems/minimum-absolute-difference-in-bst/
# Runtime  : 0 ms (beats 0%)
# Memory   : 12416000 (beats 0%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def getMinimumDifference(self, root):
        self.min_diff = float('inf')
        self.prev = None
        
        def inorder(node):
            if not node:
                return
            
            # Traverse left subtree
            inorder(node.left)
            
            # Process current node
            if self.prev is not None:
                self.min_diff = min(self.min_diff, node.val - self.prev)
            self.prev = node.val
            
            # Traverse right subtree
            inorder(node.right)
            
        inorder(root)
        return self.min_diff