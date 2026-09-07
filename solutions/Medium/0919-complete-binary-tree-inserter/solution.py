# ──────────────────────────────────────────────────
# Problem  : 919. Complete Binary Tree Inserter
# Difficulty: Medium
# Tags     : Tree, Breadth-First Search, Design, Binary Tree
# Link     : https://leetcode.com/problems/complete-binary-tree-inserter/
# Runtime  : 0 ms (beats 0%)
# Memory   : 12356000 (beats 0%)
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

class CBTInserter(object):

    def __init__(self, root):
        """
        :type root: Optional[TreeNode]
        """
        self.root = root
        self.deque = deque()
        
        # Level-order traversal to find all nodes with < 2 children
        q = deque([root])
        while q:
            node = q.popleft()
            if not node.left or not node.right:
                self.deque.append(node)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

    def insert(self, val):
        """
        :type val: int
        :rtype: int
        """
        node = TreeNode(val)
        parent = self.deque[0]
        
        if not parent.left:
            parent.left = node
        else:
            parent.right = node
            self.deque.popleft()  # Parent now has both children
            
        self.deque.append(node)
        return parent.val

    def get_root(self):
        """
        :rtype: Optional[TreeNode]
        """
        return self.root

# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(val)
# param_2 = obj.get_root()