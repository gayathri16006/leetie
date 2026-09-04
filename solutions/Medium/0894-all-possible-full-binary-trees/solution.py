# ──────────────────────────────────────────────────
# Problem  : 894. All Possible Full Binary Trees
# Difficulty: Medium
# Tags     : Dynamic Programming, Tree, Recursion, Memoization, Binary Tree
# Link     : https://leetcode.com/problems/all-possible-full-binary-trees/
# Runtime  : 0 ms (beats 0%)
# Memory   : 12304000 (beats 0%)
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
    def __init__(self):
        self.memo = {1: [TreeNode(0)]}

    def allPossibleFBT(self, n):
        """
        :type n: int
        :rtype: List[Optional[TreeNode]]
        """
        # An FBT must have an odd number of nodes
        if n % 2 == 0:
            return []

        if n in self.memo:
            return self.memo[n]

        res = []
        # Left subtree can take odd number of nodes from 1 to n - 2
        for left_nodes in range(1, n, 2):
            right_nodes = n - 1 - left_nodes
            
            left_subtrees = self.allPossibleFBT(left_nodes)
            right_subtrees = self.allPossibleFBT(right_nodes)

            for left in left_subtrees:
                for right in right_subtrees:
                    root = TreeNode(0)
                    root.left = left
                    root.right = right
                    res.append(root)

        self.memo[n] = res
        return res