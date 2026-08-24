# ──────────────────────────────────────────────────
# Problem  : 558. Logical OR of Two Binary Grids Represented as Quad-Trees
# Difficulty: Medium
# Tags     : Divide and Conquer, Tree
# Link     : https://leetcode.com/problems/logical-or-of-two-binary-grids-represented-as-quad-trees/
# Runtime  : 51 ms (beats 49%)
# Memory   : 13296000 (beats 81%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

"""
# Definition for a QuadTree node.
class Node(object):
    def __init__(self, val, isLeaf, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution(object):
    def intersect(self, quadTree1, quadTree2):
        """
        :type quadTree1: Node
        :type quadTree2: Node
        :rtype: Node
        """
        # Base case: if quadTree1 is a leaf
        if quadTree1.isLeaf:
            # 1 OR anything is 1
            if quadTree1.val:
                return quadTree1
            # 0 OR quadTree2 is quadTree2
            return quadTree2
        
        # Base case: if quadTree2 is a leaf
        if quadTree2.isLeaf:
            if quadTree2.val:
                return quadTree2
            return quadTree1

        # Recursive step: recursively compute OR for all 4 quadrants
        tl = self.intersect(quadTree1.topLeft, quadTree2.topLeft)
        tr = self.intersect(quadTree1.topRight, quadTree2.topRight)
        bl = self.intersect(quadTree1.bottomLeft, quadTree2.bottomLeft)
        br = self.intersect(quadTree1.bottomRight, quadTree2.bottomRight)

        # Merge check: if all four quadrants are leaves with the same value
        if tl.isLeaf and tr.isLeaf and bl.isLeaf and br.isLeaf and (tl.val == tr.val == bl.val == br.val):
            return Node(tl.val, True, None, None, None, None)

        # Otherwise, form a non-leaf parent node
        return Node(False, False, tl, tr, bl, br)