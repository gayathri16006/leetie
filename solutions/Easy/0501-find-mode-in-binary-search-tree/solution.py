# ──────────────────────────────────────────────────
# Problem  : 501. Find Mode in Binary Search Tree
# Difficulty: Easy
# Tags     : Tree, Depth-First Search, Binary Search Tree, Binary Tree
# Link     : https://leetcode.com/problems/find-mode-in-binary-search-tree/
# Runtime  : 0 ms (beats 0%)
# Memory   : 12388000 (beats 0%)
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
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.prev = None
        self.curr_count = 0
        self.max_count = 0
        self.modes = []

        def inorder(node):
            if not node:
                return

            inorder(node.left)

            # Update count for the current node value
            if self.prev is not None and node.val == self.prev:
                self.curr_count += 1
            else:
                self.curr_count = 1
            
            self.prev = node.val

            # Compare current streak with the maximum frequency found so far
            if self.curr_count > self.max_count:
                self.max_count = self.curr_count
                self.modes = [node.val]
            elif self.curr_count == self.max_count:
                self.modes.append(node.val)

            inorder(node.right)

        inorder(root)
        return self.modes