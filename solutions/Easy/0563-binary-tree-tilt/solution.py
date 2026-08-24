# ──────────────────────────────────────────────────
# Problem  : 563. Binary Tree Tilt
# Difficulty: Easy
# Tags     : Tree, Depth-First Search, Binary Tree, DP on Trees
# Link     : https://leetcode.com/problems/binary-tree-tilt/
# Runtime  : 0 ms (beats 0%)
# Memory   : 12356000 (beats 0%)
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
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.total_tilt = 0

        def subtree_sum(node):
            if not node:
                return 0

            # Compute sum of left and right subtrees
            left_sum = subtree_sum(node.left)
            right_sum = subtree_sum(node.right)

            # Node's tilt is |left_sum - right_sum|
            self.total_tilt += abs(left_sum - right_sum)

            # Return total sum of values rooted at this node
            return node.val + left_sum + right_sum

        subtree_sum(root)
        return self.total_tilt