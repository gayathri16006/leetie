// ──────────────────────────────────────────────────
// Problem  : 989. Add to Array-Form of Integer
// Difficulty: Easy
// Tags     : Array, Math
// Link     : https://leetcode.com/problems/add-to-array-form-of-integer/
// Runtime  : 3 ms (beats 72%)
// Memory   : 47924000 (beats 19%)
// Language : java
// Copyright: (c) 2026 gayathri16006. All rights reserved.
// Synced by: leetie
// ──────────────────────────────────────────────────

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

class Solution {
    public List<Integer> addToArrayForm(int[] num, int k) {
        List<Integer> result = new ArrayList<>();
        int i = num.length - 1;

        // Process digits from right to left while elements or carry in k remain
        while (i >= 0 || k > 0) {
            if (i >= 0) {
                k += num[i];
                i--;
            }
            // Append the last digit of the current sum
            result.add(k % 10);
            // Carry over the remaining digits
            k /= 10;
        }

        // Reverse to restore most significant digit first
        Collections.reverse(result);
        return result;
    }
}