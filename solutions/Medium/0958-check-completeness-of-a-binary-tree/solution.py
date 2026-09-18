# ──────────────────────────────────────────────────
# Problem  : 958. Check Completeness of a Binary Tree
# Difficulty: Medium
# Tags     : Tree, Breadth-First Search, Binary Tree
# Link     : https://leetcode.com/problems/check-completeness-of-a-binary-tree/
# Runtime  : 0 ms (beats 100%)
# Memory   : 12424000 (beats 55%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isCompleteTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        queue = deque([root])
        seen_null = False

        while queue:
            node = queue.popleft()

            if not node:
                seen_null = True
            else:
                if seen_null:
                    return False
                queue.append(node.left)
                queue.append(node.right)

        return True