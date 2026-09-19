// ──────────────────────────────────────────────────
// Problem  : 987. Vertical Order Traversal of a Binary Tree
// Difficulty: Hard
// Tags     : Hash Table, Tree, Depth-First Search, Breadth-First Search, Sorting, Binary Tree
// Link     : https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/
// Runtime  : 1 ms (beats 0%)
// Memory   : 42592000 (beats 0%)
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
import java.util.*;

class Solution {
    static class NodeInfo {
        int row;
        int col;
        int val;

        NodeInfo(int row, int col, int val) {
            this.row = row;
            this.col = col;
            this.val = val;
        }
    }

    public List<List<Integer>> verticalTraversal(TreeNode root) {
        List<NodeInfo> nodes = new ArrayList<>();
        
        // Traverse and collect coordinates
        dfs(root, 0, 0, nodes);

        // Sort by: col ASC -> row ASC -> val ASC
        Collections.sort(nodes, (a, b) -> {
            if (a.col != b.col) {
                return Integer.compare(a.col, b.col);
            }
            if (a.row != b.row) {
                return Integer.compare(a.row, b.row);
            }
            return Integer.compare(a.val, b.val);
        });

        // Group by column
        List<List<Integer>> result = new ArrayList<>();
        int prevCol = Integer.MIN_VALUE;

        for (NodeInfo node : nodes) {
            if (node.col != prevCol) {
                result.add(new ArrayList<>());
                prevCol = node.col;
            }
            result.get(result.size() - 1).add(node.val);
        }

        return result;
    }

    private void dfs(TreeNode node, int row, int col, List<NodeInfo> list) {
        if (node == null) return;
        list.add(new NodeInfo(row, col, node.val));
        dfs(node.left, row + 1, col - 1, list);
        dfs(node.right, row + 1, col + 1, list);
    }
}