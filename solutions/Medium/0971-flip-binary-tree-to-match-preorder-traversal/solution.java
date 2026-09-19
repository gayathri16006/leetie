// ──────────────────────────────────────────────────
// Problem  : 971. Flip Binary Tree To Match Preorder Traversal
// Difficulty: Medium
// Tags     : Tree, Depth-First Search, Binary Tree
// Link     : https://leetcode.com/problems/flip-binary-tree-to-match-preorder-traversal/
// Runtime  : 0 ms (beats 100%)
// Memory   : 43880000 (beats 52%)
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
    private List<Integer> flipped = new ArrayList<>();

    public List<Integer> flipMatchVoyage(TreeNode root, int[] voyage) {
        flipped.clear();
        index = 0;
        
        if (dfs(root, voyage)) {
            return flipped;
        }
        return Arrays.asList(-1);
    }

    private boolean dfs(TreeNode node, int[] voyage) {
        if (node == null) {
            return true;
        }

        // Current node's value must match the current voyage element
        if (node.val != voyage[index++]) {
            return false;
        }

        // If left child exists and doesn't match next value, flip
        if (node.left != null && node.left.val != voyage[index]) {
            flipped.add(node.val);
           
            return dfs(node.right, voyage) && dfs(node.left, voyage);
        }

       
        return dfs(node.left, voyage) && dfs(node.right, voyage);
    }
}