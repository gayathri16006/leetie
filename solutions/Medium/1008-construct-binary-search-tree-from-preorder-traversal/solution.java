// ──────────────────────────────────────────────────
// Problem  : 1008. Construct Binary Search Tree from Preorder Traversal
// Difficulty: Medium
// Tags     : Array, Stack, Tree, Binary Search Tree, Monotonic Stack, Binary Tree
// Link     : https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/
// Runtime  : 0 ms (beats 100%)
// Memory   : 43432000 (beats 57%)
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
    private int index = 0;

    public TreeNode bstFromPreorder(int[] preorder) {
        return buildBST(preorder, Integer.MAX_VALUE);
    }

    private TreeNode buildBST(int[] preorder, int bound) {
        if (index >= preorder.length || preorder[index] > bound) {
            return null;
        }

        TreeNode root = new TreeNode(preorder[index++]);
        root.left = buildBST(preorder, root.val);
        root.right = buildBST(preorder, bound);

        return root;
    }
}