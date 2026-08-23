# ──────────────────────────────────────────────────
# Problem  : 538. Convert BST to Greater Tree
# Difficulty: Medium
# Tags     : Tree, Depth-First Search, Binary Search Tree, Binary Tree
# Link     : https://leetcode.com/problems/convert-bst-to-greater-tree/
# Runtime  : 11 ms (beats 23%)
# Memory   : 17492000 (beats 70%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def convertBST(self, root):
        self.running_sum = 0
        
        def reverse_inorder(node):
            if not node:
                return
            
            # 1. Traverse right subtree first (larger values)
            reverse_inorder(node.right)
            
            # 2. Update current node
            self.running_sum += node.val
            node.val = self.running_sum
            
            # 3. Traverse left subtree (smaller values)
            reverse_inorder(node.left)
            
        reverse_inorder(root)
        return root