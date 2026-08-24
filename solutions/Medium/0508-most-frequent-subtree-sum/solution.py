# ──────────────────────────────────────────────────
# Problem  : 508. Most Frequent Subtree Sum
# Difficulty: Medium
# Tags     : Hash Table, Tree, Depth-First Search, Binary Tree, DP on Trees
# Link     : https://leetcode.com/problems/most-frequent-subtree-sum/
# Runtime  : 3 ms (beats 78%)
# Memory   : 21572000 (beats 38%)
# Language : python3
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

from collections import Counter
from typing import Optional, List

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        counts = Counter()
        
        def get_subtree_sum(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            
            # Post-order: sum = node.val + left_subtree_sum + right_subtree_sum
            current_sum = node.val + get_subtree_sum(node.left) + get_subtree_sum(node.right)
            counts[current_sum] += 1
            return current_sum

        get_subtree_sum(root)
        
        max_freq = max(counts.values())
        return [s for s, freq in counts.items() if freq == max_freq]