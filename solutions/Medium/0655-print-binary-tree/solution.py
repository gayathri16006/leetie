# ──────────────────────────────────────────────────
# Problem  : 655. Print Binary Tree
# Difficulty: Medium
# Tags     : Tree, Depth-First Search, Breadth-First Search, Binary Tree
# Link     : https://leetcode.com/problems/print-binary-tree/
# Runtime  : 0 ms (beats 100%)
# Memory   : 12348000 (beats 60%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def printTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[str]]
        """
        # 1. Calculate the height of the tree (0-indexed)
        def get_height(node):
            if not node:
                return -1
            return 1 + max(get_height(node.left), get_height(node.right))
        
        height = get_height(root)
        m = height + 1
        n = (1 << (height + 1)) - 1
        
        # 2. Initialize matrix with empty strings
        res = [["" for _ in range(n)] for _ in range(m)]
        
        # 3. Populate matrix using DFS
        def populate(node, r, c):
            if not node:
                return
            
            res[r][c] = str(node.val)
            
            # Recurse for children if they exist
            if node.left:
                populate(node.left, r + 1, c - (1 << (height - r - 1)))
            if node.right:
                populate(node.right, r + 1, c + (1 << (height - r - 1)))
        
        populate(root, 0, (n - 1) // 2)
        return res