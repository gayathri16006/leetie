// ──────────────────────────────────────────────────
// Problem  : 986. Interval List Intersections
// Difficulty: Medium
// Tags     : Array, Two Pointers, Sweep Line
// Link     : https://leetcode.com/problems/interval-list-intersections/
// Runtime  : 3 ms (beats 99%)
// Memory   : 47516000 (beats 19%)
// Language : java
// Copyright: (c) 2026 gayathri16006. All rights reserved.
// Synced by: leetie
// ──────────────────────────────────────────────────

import java.util.ArrayList;
import java.util.List;

class Solution {
    public int[][] intervalIntersection(int[][] firstList, int[][] secondList) {
        List<int[]> result = new ArrayList<>();
        int i = 0, j = 0;

        while (i < firstList.length && j < secondList.length) {
            // Find the overlapping range
            int start = Math.max(firstList[i][0], secondList[j][0]);
            int end = Math.min(firstList[i][1], secondList[j][1]);

            // If a valid intersection exists
            if (start <= end) {
                result.add(new int[]{start, end});
            }

            // Move the pointer of the interval that ends first
            if (firstList[i][1] < secondList[j][1]) {
                i++;
            } else {
                j++;
            }
        }

        return result.toArray(new int[result.size()][]);
    }
}