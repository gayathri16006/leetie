# ──────────────────────────────────────────────────
# Problem  : 863. All Nodes Distance K in Binary Tree
# Difficulty: Medium
# Tags     : Hash Table, Tree, Depth-First Search, Breadth-First Search, Binary Tree
# Link     : https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/
# Runtime  : 20 ms (beats 0%)
# Memory   : 12216000 (beats 0%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def distanceK(self, root, target, k):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type k: int
        :rtype: List[int]
        """
        if not root:
            return []

        # Step 1: Map each node to its parent using DFS
        parent_map = {}
        def map_parents(node, parent):
            if node:
                parent_map[node] = parent
                map_parents(node.left, node)
                map_parents(node.right, node)

        map_parents(root, None)

        # Step 2: BFS starting from target node
        queue = deque([(target, 0)])
        visited = {target}

        while queue:
            # If front element is at distance k, return all elements at this layer
            if queue[0][1] == k:
                return [node.val for node, dist in queue]

            node, dist = queue.popleft()

            # Explore left child, right child, and parent
            for neighbor in (node.left, node.right, parent_map.get(node)):
                if neighbor and neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, dist + 1))

        return []