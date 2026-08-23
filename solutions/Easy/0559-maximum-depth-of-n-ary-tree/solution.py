# ──────────────────────────────────────────────────
# Problem  : 559. Maximum Depth of N-ary Tree
# Difficulty: Easy
# Tags     : Tree, Depth-First Search, Breadth-First Search
# Link     : https://leetcode.com/problems/maximum-depth-of-n-ary-tree/
# Runtime  : 15 ms (beats 0%)
# Memory   : 12380000 (beats 0%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def maxDepth(self, root):
        if not root:
            return 0
        
        if not root.children:
            return 1
            
        return 1 + max(self.maxDepth(child) for child in root.children)