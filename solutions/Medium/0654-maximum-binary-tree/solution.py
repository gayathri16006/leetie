# ──────────────────────────────────────────────────
# Problem  : 654. Maximum Binary Tree
# Difficulty: Medium
# Tags     : Array, Divide and Conquer, Stack, Tree, Monotonic Stack, Binary Tree, Cartesian Tree
# Link     : https://leetcode.com/problems/maximum-binary-tree/
# Runtime  : 0 ms (beats 0%)
# Memory   : 19384000 (beats 0%)
# Language : python3
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

from typing import List, Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def build(left: int, right: int) -> Optional[TreeNode]:
            if left > right:
                return None
            
            # Find the maximum element and its index in current range
            max_idx = left
            for i in range(left + 1, right + 1):
                if nums[i] > nums[max_idx]:
                    max_idx = i
                    
            root = TreeNode(nums[max_idx])
            root.left = build(left, max_idx - 1)
            root.right = build(max_idx + 1, right)
            
            return root
            
        return build(0, len(nums) - 1)