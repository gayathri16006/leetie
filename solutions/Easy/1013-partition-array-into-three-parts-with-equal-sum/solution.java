// ──────────────────────────────────────────────────
// Problem  : 1013. Partition Array Into Three Parts With Equal Sum
// Difficulty: Easy
// Tags     : Array, Greedy
// Link     : https://leetcode.com/problems/partition-array-into-three-parts-with-equal-sum/
// Runtime  : 0 ms (beats 0%)
// Memory   : 42516000 (beats 0%)
// Language : java
// Copyright: (c) 2026 gayathri16006. All rights reserved.
// Synced by: leetie
// ──────────────────────────────────────────────────

class Solution {
    public boolean canThreePartsEqualSum(int[] arr) {
        int totalSum = 0;
        for (int x : arr) {
            totalSum += x;
        }

        // If total sum is not divisible by 3, cannot partition into 3 equal parts
        if (totalSum % 3 != 0) {
            return false;
        }

        int target = totalSum / 3;
        int currentSum = 0;
        int count = 0;

        for (int x : arr) {
            currentSum += x;
            if (currentSum == target) {
                count++;
                currentSum = 0;
            }
        }

        // We need at least 3 parts (if count > 3, extra parts must sum to 0)
        return count >= 3;
    }
}