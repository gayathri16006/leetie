// ──────────────────────────────────────────────────
// Problem  : 1130. Minimum Cost Tree From Leaf Values
// Difficulty: Medium
// Tags     : Array, Dynamic Programming, Stack, Greedy, Monotonic Stack, Cartesian Tree
// Link     : https://leetcode.com/problems/minimum-cost-tree-from-leaf-values/
// Runtime  : 1 ms (beats 98%)
// Memory   : 42988000 (beats 72%)
// Language : java
// Copyright: (c) 2026 gayathri16006. All rights reserved.
// Synced by: leetie
// ──────────────────────────────────────────────────

import java.util.ArrayDeque;
import java.util.Deque;

class Solution {
    public int mctFromLeafValues(int[] arr) {
        int totalCost = 0;
        Deque<Integer> stack = new ArrayDeque<>();
        
       
        stack.push(Integer.MAX_VALUE);

        for (int val : arr) {
            
            while (stack.peek() <= val) {
                int mid = stack.pop();
                
                totalCost += mid * Math.min(stack.peek(), val);
            }
            stack.push(val);
        }

        
        while (stack.size() > 2) {
            totalCost += stack.pop() * stack.peek();
        }

        return totalCost;
    }
}