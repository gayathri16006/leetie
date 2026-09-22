// ──────────────────────────────────────────────────
// Problem  : 3525. Find X Value of Array II
// Difficulty: Hard
// Tags     : Array, Math, Segment Tree
// Link     : https://leetcode.com/problems/find-x-value-of-array-ii/
// Runtime  : 285 ms (beats 21%)
// Memory   : 284616000 (beats 26%)
// Language : java
// Copyright: (c) 2026 gayathri16006. All rights reserved.
// Synced by: leetie
// ──────────────────────────────────────────────────

class Solution {
    static class Node {
        int prod;
        int[] count;

        Node(int k) {
            count = new int[k];
        }
    }

    private int k;
    private Node[] tree;
    private int n;

    private Node merge(Node left, Node right) {
        if (left == null) return right;
        if (right == null) return left;

        Node res = new Node(k);
        res.prod = (int) ((1L * left.prod * right.prod) % k);

        // Copy counts from left child
        for (int i = 0; i < k; i++) {
            res.count[i] += left.count[i];
        }

        // Multiply right child's prefix products by left child's total product
        for (int i = 0; i < k; i++) {
            int newRem = (int) ((1L * left.prod * i) % k);
            res.count[newRem] += right.count[i];
        }

        return res;
    }

    private void build(int[] nums, int node, int start, int end) {
        tree[node] = new Node(k);
        if (start == end) {
            int rem = nums[start] % k;
            tree[node].prod = rem;
            tree[node].count[rem] = 1;
            return;
        }

        int mid = start + (end - start) / 2;
        int leftChild = 2 * node;
        int rightChild = 2 * node + 1;

        build(nums, leftChild, start, mid);
        build(nums, rightChild, mid + 1, end);

        tree[node] = merge(tree[leftChild], tree[rightChild]);
    }

    private void update(int node, int start, int end, int idx, int val) {
        if (start == end) {
            int rem = val % k;
            tree[node] = new Node(k);
            tree[node].prod = rem;
            tree[node].count[rem] = 1;
            return;
        }

        int mid = start + (end - start) / 2;
        int leftChild = 2 * node;
        int rightChild = 2 * node + 1;

        if (idx <= mid) {
            update(leftChild, start, mid, idx, val);
        } else {
            update(rightChild, mid + 1, end, idx, val);
        }

        tree[node] = merge(tree[leftChild], tree[rightChild]);
    }

    private Node query(int node, int start, int end, int l, int r) {
        if (r < start || end < l) return null;
        if (l <= start && end <= r) return tree[node];

        int mid = start + (end - start) / 2;
        Node leftRes = query(2 * node, start, mid, l, r);
        Node rightRes = query(2 * node + 1, mid + 1, end, l, r);

        return merge(leftRes, rightRes);
    }

    public int[] resultArray(int[] nums, int k, int[][] queries) {
        this.n = nums.length;
        this.k = k;
        this.tree = new Node[4 * n];

        build(nums, 1, 0, n - 1);

        int[] ans = new int[queries.length];
        for (int i = 0; i < queries.length; i++) {
            int idx = queries[i][0];
            int val = queries[i][1];
            int start = queries[i][2];
            int x = queries[i][3];

            
            update(1, 0, n - 1, idx, val);

           
            Node res = query(1, 0, n - 1, start, n - 1);
            ans[i] = res != null ? res.count[x] : 0;
        }

        return ans;
    }
}