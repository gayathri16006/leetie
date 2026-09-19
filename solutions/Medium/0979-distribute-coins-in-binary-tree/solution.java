// ──────────────────────────────────────────────────
// Problem  : 979. Distribute Coins in Binary Tree
// Difficulty: Medium
// Tags     : Tree, Depth-First Search, Binary Tree, DP on Trees
// Link     : https://leetcode.com/problems/distribute-coins-in-binary-tree/
// Runtime  : 0 ms (beats 100%)
// Memory   : 44084000 (beats 15%)
// Language : java
// Copyright: (c) 2026 gayathri16006. All rights reserved.
// Synced by: leetie
// ──────────────────────────────────────────────────

class Solution {
    private int moves = 0;

    public int distributeCoins(TreeNode root) {
        moves = 0;
        dfs(root);
        return moves;
    }

    private int dfs(TreeNode node) {
        if (node == null) return 0;

        int left = dfs(node.left);
        int right = dfs(node.right);

        // Every excess or deficit of coins must cross the edge between node and its children
        moves += Math.abs(left) + Math.abs(right);

        // Net balance of coins from this subtree to pass to parent:
        // current coins + left balance + right balance - 1 (kept for this node)
        return node.val + left + right - 1;
    }
}