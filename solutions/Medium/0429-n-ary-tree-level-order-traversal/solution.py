# ──────────────────────────────────────────────────
# Problem  : 429. N-ary Tree Level Order Traversal
# Difficulty: Medium
# Tags     : Tree, Breadth-First Search
# Link     : https://leetcode.com/problems/n-ary-tree-level-order-traversal/
# Runtime  : 41 ms (beats 18%)
# Memory   : 15560000 (beats 41%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

from collections import deque


class Solution(object):

    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            level_size = len(queue)
            current_level = []

            for _ in range(level_size):
                node = queue.popleft()
                current_level.append(node.val)

                if node.children:
                    queue.extend(node.children)

            result.append(current_level)

        return result