// ──────────────────────────────────────────────────
// Problem  : 968. Binary Tree Cameras
// Difficulty: Hard
// Tags     : Dynamic Programming, Tree, Depth-First Search, Binary Tree, DP on Trees
// Link     : https://leetcode.com/problems/binary-tree-cameras/
// Runtime  : 0 ms (beats 100%)
// Memory   : 44328000 (beats 94%)
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
            return 2; 
        }

        int left = dfs(node.left);
        int right = dfs(node.right);

        
        if (left == 0 || right == 0) {
            cameras++;
            return 1;
        }

        
        if (left == 1 || right == 1) {
            return 2;
        }

       
        return 0;
    }
}