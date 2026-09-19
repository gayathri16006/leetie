// ──────────────────────────────────────────────────
// Problem  : 968. Binary Tree Cameras
// Difficulty: Hard
// Tags     : Dynamic Programming, Tree, Depth-First Search, Binary Tree, DP on Trees
// Link     : https://leetcode.com/problems/binary-tree-cameras/
// Runtime  : 0 ms (beats 0%)
// Memory   : 42948000 (beats 0%)
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
    private int cameras = 0;

    // States:
    // 0 -> Uncovered
    // 1 -> Has camera
    // 2 -> Covered (no camera)
    public int minCameraCover(TreeNode root) {
        if (dfs(root) == 0) {
            cameras++;
        }
        return cameras;
    }

    private int dfs(TreeNode node) {
        if (node == null) {
            return 2; // Null nodes are considered covered
        }

        int left = dfs(node.left);
        int right = dfs(node.right);

        // If any child is uncovered, place a camera here
        if (left == 0 || right == 0) {
            cameras++;
            return 1;
        }

        // If any child has a camera, this node is covered
        if (left == 1 || right == 1) {
            return 2;
        }

       
        return 0;
    }
}