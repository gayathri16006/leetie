# ──────────────────────────────────────────────────
# Problem  : 337. House Robber III
# Difficulty: Medium
# Tags     : Dynamic Programming, Tree, Depth-First Search, Binary Tree, DP on Trees
# Link     : https://leetcode.com/problems/house-robber-iii/
# Runtime  : 4 ms (beats 80%)
# Memory   : 16360000 (beats 98%)
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

    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def dfs(node):
            # Base case: returns (rob_this_node, not_rob_this_node)
            if not node:
                return (0, 0)

            left_rob, left_not_rob = dfs(node.left)
            right_rob, right_not_rob = dfs(node.right)

            # If this node is robbed, children cannot be robbed
            rob_curr = node.val + left_not_rob + right_not_rob

            # If this node is not robbed, children can either be robbed or not
            not_rob_curr = max(left_rob, left_not_rob) + max(
                right_rob, right_not_rob
            )

            return (rob_curr, not_rob_curr)

        return max(dfs(root))