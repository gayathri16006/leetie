// ──────────────────────────────────────────────────
// Problem  : 976. Largest Perimeter Triangle
// Difficulty: Easy
// Tags     : Array, Math, Greedy, Sorting, Quicksort, Polygons
// Link     : https://leetcode.com/problems/largest-perimeter-triangle/
// Runtime  : 11 ms (beats 98%)
// Memory   : 47920000 (beats 7%)
// Language : java
// Copyright: (c) 2026 gayathri16006. All rights reserved.
// Synced by: leetie
// ──────────────────────────────────────────────────

import java.util.Arrays;

class Solution {
    public int largestPerimeter(int[] nums) {
        Arrays.sort(nums);

        
        for (int i = nums.length - 1; i >= 2; i--) {
            if (nums[i - 2] + nums[i - 1] > nums[i]) {
                return nums[i - 2] + nums[i - 1] + nums[i];
            }
        }

        return 0;
    }
}