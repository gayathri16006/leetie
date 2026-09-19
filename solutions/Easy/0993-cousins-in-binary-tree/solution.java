// ──────────────────────────────────────────────────
// Problem  : 993. Cousins in Binary Tree
// Difficulty: Easy
// Tags     : Tree, Depth-First Search, Breadth-First Search, Binary Tree
// Link     : https://leetcode.com/problems/cousins-in-binary-tree/
// Runtime  : 0 ms (beats 100%)
// Memory   : 43468000 (beats 8%)
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
    private int xDepth = -1;
    private int yDepth = -2;
    private TreeNode xParent = null;
    private TreeNode yParent = null;

    public boolean isCousins(TreeNode root, int x, int y) {
        dfs(root, null, 0, x, y);
        return xDepth == yDepth && xParent != yParent;
    }

    private void dfs(TreeNode node, TreeNode parent, int depth, int x, int y) {
        if (node == null) {
            return;
        }

        if (node.val == x) {
            xDepth = depth;
            xParent = parent;
        } else if (node.val == y) {
            yDepth = depth;
            yParent = parent;
        }

        // Early exit if both nodes have been found
        if (xParent != null && yParent != null) {
            return;
        }

        dfs(node.left, node, depth + 1, x, y);
        dfs(node.right, node, depth + 1, x, y);
    }
}