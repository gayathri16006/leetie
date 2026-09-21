// ──────────────────────────────────────────────────
// Problem  : 1022. Sum of Root To Leaf Binary Numbers
// Difficulty: Easy
// Tags     : Tree, Depth-First Search, Binary Tree
// Link     : https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/
// Runtime  : 0 ms (beats 100%)
// Memory   : 43640000 (beats 70%)
// Language : java
// Copyright: (c) 2026 gayathri16006. All rights reserved.
// Synced by: leetie
// ──────────────────────────────────────────────────

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public int sumRootToLeaf(TreeNode root) {
        return dfs(root, 0);
    }

    private int dfs(TreeNode node, int currentVal) {
        if (node == null) {
            return 0;
        }

        
        currentVal = (currentVal << 1) | node.val;

        
        if (node.left == null && node.right == null) {
            return currentVal;
        }

        return dfs(node.left, currentVal) + dfs(node.right, currentVal);
    }
}