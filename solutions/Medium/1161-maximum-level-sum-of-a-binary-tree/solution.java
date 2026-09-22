// ──────────────────────────────────────────────────
// Problem  : 1161. Maximum Level Sum of a Binary Tree
// Difficulty: Medium
// Tags     : Tree, Depth-First Search, Breadth-First Search, Binary Tree
// Link     : https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/
// Runtime  : 0 ms (beats 0%)
// Memory   : 42424000 (beats 0%)
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
import java.util.ArrayDeque;
import java.util.Queue;

class Solution {
    public int maxLevelSum(TreeNode root) {
        if (root == null) return 0;

        Queue<TreeNode> queue = new ArrayDeque<>();
        queue.offer(root);

        int maxSum = Integer.MIN_VALUE;
        int bestLevel = 1;
        int currentLevel = 1;

        while (!queue.isEmpty()) {
            int size = queue.size();
            int currentLevelSum = 0;

            for (int i = 0; i < size; i++) {
                TreeNode node = queue.poll();
                currentLevelSum += node.val;

                if (node.left != null) {
                    queue.offer(node.left);
                }
                if (node.right != null) {
                    queue.offer(node.right);
                }
            }

            // Using strictly greater ensures we keep the smallest level in case of ties
            if (currentLevelSum > maxSum) {
                maxSum = currentLevelSum;
                bestLevel = currentLevel;
            }

            currentLevel++;
        }

        return bestLevel;
    }
}