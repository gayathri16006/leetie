// ──────────────────────────────────────────────────
// Problem  : 988. Smallest String Starting From Leaf
// Difficulty: Medium
// Tags     : String, Backtracking, Tree, Depth-First Search, Binary Tree
// Link     : https://leetcode.com/problems/smallest-string-starting-from-leaf/
// Runtime  : 0 ms (beats 0%)
// Memory   : 42920000 (beats 0%)
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
    private String smallest = null;

    public String smallestFromLeaf(TreeNode root) {
        dfs(root, new StringBuilder());
        return smallest;
    }

    private void dfs(TreeNode node, StringBuilder currentPath) {
        if (node == null) {
            return;
        }

        // Append current character
        currentPath.append((char) ('a' + node.val));

        // Check if it's a leaf node
        if (node.left == null && node.right == null) {
            // Reverse to get the string from leaf to root
            String candidate = new StringBuilder(currentPath).reverse().toString();
            if (smallest == null || candidate.compareTo(smallest) < 0) {
                smallest = candidate;
            }
        } else {
            dfs(node.left, currentPath);
            dfs(node.right, currentPath);
        }

        // Backtrack
        currentPath.deleteCharAt(currentPath.length() - 1);
    }
}