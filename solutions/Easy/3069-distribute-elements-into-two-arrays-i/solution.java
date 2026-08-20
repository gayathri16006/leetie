// ──────────────────────────────────────────────────
// Problem  : 3069. Distribute Elements Into Two Arrays I
// Difficulty: Easy
// Tags     : Array, Simulation
// Link     : https://leetcode.com/problems/distribute-elements-into-two-arrays-i/
// Runtime  : 2 ms (beats 57%)
// Memory   : 46572000 (beats 81%)
// Language : java
// Copyright: (c) 2026 gayathri16006. All rights reserved.
// Synced by: leetie
// ──────────────────────────────────────────────────

import java.util.ArrayList;
import java.util.List;

class Solution {
    public int[] resultArray(int[] nums) {
        List<Integer> arr1 = new ArrayList<>();
        List<Integer> arr2 = new ArrayList<>();

        // 1st operation: append nums[0] to arr1
        arr1.add(nums[0]);
        // 2nd operation: append nums[1] to arr2
        arr2.add(nums[1]);

        // Subsequent operations from index 2 onwards
        for (int i = 2; i < nums.length; i++) {
            if (arr1.get(arr1.size() - 1) > arr2.get(arr2.size() - 1)) {
                arr1.add(nums[i]);
            } else {
                arr2.add(nums[i]);
            }
        }

        // Concatenate arr1 and arr2 into result array
        int[] result = new int[nums.length];
        int idx = 0;

        for (int val : arr1) {
            result[idx++] = val;
        }
        for (int val : arr2) {
            result[idx++] = val;
        }

        return result;
    }
}