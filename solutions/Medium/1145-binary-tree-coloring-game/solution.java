// ──────────────────────────────────────────────────
// Problem  : 1145. Binary Tree Coloring Game
// Difficulty: Medium
// Tags     : Tree, Depth-First Search, Binary Tree
// Link     : https://leetcode.com/problems/binary-tree-coloring-game/
// Runtime  : 0 ms (beats 100%)
// Memory   : 43276000 (beats 43%)
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
    private int leftCount = 0;
    private int rightCount = 0;

    public boolean btreeGameWinningMove(TreeNode root, int n, int x) {
        countNodes(root, x);
        
        int parentCount = n - 1 - leftCount - rightCount;
        int maxSubtree = Math.max(parentCount, Math.max(leftCount, rightCount));

        return maxSubtree > n / 2;
    }

    private int countNodes(TreeNode node, int x) {
        if (node == null) return 0;

        int left = countNodes(node.left, x);
        int right = countNodes(node.right, x);

        if (node.val == x) {
            leftCount = left;
            rightCount = right;
        }

        return 1 + left + right;
    }
}