// ──────────────────────────────────────────────────
// Problem  : 998. Maximum Binary Tree II
// Difficulty: Medium
// Tags     : Tree, Binary Tree
// Link     : https://leetcode.com/problems/maximum-binary-tree-ii/
// Runtime  : 0 ms (beats 100%)
// Memory   : 43536000 (beats 30%)
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
    public TreeNode insertIntoMaxTree(TreeNode root, int val) {
        // If tree is empty or val is greater than the current root
        if (root == null || val > root.val) {
            TreeNode node = new TreeNode(val);
            node.left = root;
            return node;
        }

        // Otherwise, val must belong in the right subtree
        root.right = insertIntoMaxTree(root.right, val);
        return root;
    }
}