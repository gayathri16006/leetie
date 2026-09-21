// ──────────────────────────────────────────────────
// Problem  : 1018. Binary Prefix Divisible By 5
// Difficulty: Easy
// Tags     : Array, Bit Manipulation
// Link     : https://leetcode.com/problems/binary-prefix-divisible-by-5/
// Runtime  : 0 ms (beats 0%)
// Memory   : 42596000 (beats 0%)
// Language : java
// Copyright: (c) 2026 gayathri16006. All rights reserved.
// Synced by: leetie
// ──────────────────────────────────────────────────

import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<Boolean> prefixesDivBy5(int[] nums) {
        List<Boolean> ans = new ArrayList<>(nums.length);
        int remainder = 0;

        for (int bit : nums) {
            remainder = ((remainder << 1) + bit) % 5;
            ans.add(remainder == 0);
        }

        return ans;
    }
}