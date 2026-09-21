// ──────────────────────────────────────────────────
// Problem  : 1026. Maximum Difference Between Node and Ancestor
// Difficulty: Medium
// Tags     : Tree, Depth-First Search, Binary Tree
// Link     : https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/
// Runtime  : 0 ms (beats 100%)
// Memory   : 43832000 (beats 41%)
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
    public int maxAncestorDiff(TreeNode root) {
        if (root == null) {
            return 0;
        }
        return dfs(root, root.val, root.val);
    }

    private int dfs(TreeNode node, int minVal, int maxVal) {
        if (node == null) {
            return maxVal - minVal;
        }

        
        minVal = Math.min(minVal, node.val);
        maxVal = Math.max(maxVal, node.val);

       
        int leftDiff = dfs(node.left, minVal, maxVal);
        int rightDiff = dfs(node.right, minVal, maxVal);

        return Math.max(leftDiff, rightDiff);
    }
}