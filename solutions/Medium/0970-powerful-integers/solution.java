// ──────────────────────────────────────────────────
// Problem  : 970. Powerful Integers
// Difficulty: Medium
// Tags     : Hash Table, Math, Enumeration
// Link     : https://leetcode.com/problems/powerful-integers/
// Runtime  : 0 ms (beats 0%)
// Memory   : 42388000 (beats 0%)
// Language : java
// Copyright: (c) 2026 gayathri16006. All rights reserved.
// Synced by: leetie
// ──────────────────────────────────────────────────

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

class Solution {
    public List<Integer> powerfulIntegers(int x, int y, int bound) {
        Set<Integer> result = new HashSet<>();

        for (int a = 1; a < bound; a *= x) {
            for (int b = 1; a + b <= bound; b *= y) {
                result.add(a + b);
                if (y == 1) {
                    break;
                }
            }
            if (x == 1) {
                break;
            }
        }

        return new ArrayList<>(result);
    }
}