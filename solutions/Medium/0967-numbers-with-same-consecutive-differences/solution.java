// ──────────────────────────────────────────────────
// Problem  : 967. Numbers With Same Consecutive Differences
// Difficulty: Medium
// Tags     : Backtracking, Breadth-First Search
// Link     : https://leetcode.com/problems/numbers-with-same-consecutive-differences/
// Runtime  : 3 ms (beats 55%)
// Memory   : 43844000 (beats 32%)
// Language : java
// Copyright: (c) 2026 gayathri16006. All rights reserved.
// Synced by: leetie
// ──────────────────────────────────────────────────

import java.util.*;

class Solution {
    public int[] numsSameConsecDiff(int n, int k) {
       
        List<Integer> queue = new ArrayList<>();
        for (int i = 1; i <= 9; i++) {
            queue.add(i);
        }

        
        for (int level = 1; level < n; level++) {
            List<Integer> nextQueue = new ArrayList<>();
            for (int num : queue) {
                int lastDigit = num % 10;

                
                if (lastDigit + k <= 9) {
                    nextQueue.add(num * 10 + (lastDigit + k));
                }

                
                if (k > 0 && lastDigit - k >= 0) {
                    nextQueue.add(num * 10 + (lastDigit - k));
                }
            }
            queue = nextQueue;
        }

        
        int[] result = new int[queue.size()];
        for (int i = 0; i < queue.size(); i++) {
            result[i] = queue.get(i);
        }

        return result;
    }
}