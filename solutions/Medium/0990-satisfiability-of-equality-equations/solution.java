// ──────────────────────────────────────────────────
// Problem  : 990. Satisfiability of Equality Equations
// Difficulty: Medium
// Tags     : Array, String, Union-Find, Graph Theory
// Link     : https://leetcode.com/problems/satisfiability-of-equality-equations/
// Runtime  : 0 ms (beats 0%)
// Memory   : 42504000 (beats 0%)
// Language : java
// Copyright: (c) 2026 gayathri16006. All rights reserved.
// Synced by: leetie
// ──────────────────────────────────────────────────

class Solution {
    private int[] parent = new int[26];

    public boolean equationsPossible(String[] equations) {
        // Initialize Union-Find: each variable is its own parent
        for (int i = 0; i < 26; i++) {
            parent[i] = i;
        }

        // First pass: group variables connected by "=="
        for (String eq : equations) {
            if (eq.charAt(1) == '=') {
                int u = eq.charAt(0) - 'a';
                int v = eq.charAt(3) - 'a';
                union(u, v);
            }
        }

        // Second pass: verify that variables separated by "!=" are in different sets
        for (String eq : equations) {
            if (eq.charAt(1) == '!') {
                int u = eq.charAt(0) - 'a';
                int v = eq.charAt(3) - 'a';
                if (find(u) == find(v)) {
                    return false; // Contradiction found
                }
            }
        }

        return true;
    }

    private int find(int x) {
        if (parent[x] != x) {
            parent[x] = find(parent[x]); // Path compression
        }
        return parent[x];
    }

    private void union(int x, int y) {
        int rootX = find(x);
        int rootY = find(y);
        if (rootX != rootY) {
            parent[rootX] = rootY;
        }
    }
}