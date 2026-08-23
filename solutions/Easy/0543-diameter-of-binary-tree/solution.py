# ──────────────────────────────────────────────────
# Problem  : 543. Diameter of Binary Tree
# Difficulty: Easy
# Tags     : Tree, Depth-First Search, Binary Tree, DP on Trees
# Link     : https://leetcode.com/problems/diameter-of-binary-tree/
# Runtime  : 0 ms (beats 0%)
# Memory   : 12548000 (beats 0%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def diameterOfBinaryTree(self, root):
        self.max_diameter = 0
        
        def get_depth(node):
            if not node:
                return 0
            
            left_depth = get_depth(node.left)
            right_depth = get_depth(node.right)
            
            # Update the maximum diameter (number of edges = left_depth + right_depth)
            self.max_diameter = max(self.max_diameter, left_depth + right_depth)
            
            # Return height of the current subtree
            return 1 + max(left_depth, right_depth)
        
        get_depth(root)
        return self.max_diameter