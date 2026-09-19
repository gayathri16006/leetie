// ──────────────────────────────────────────────────
// Problem  : 975. Odd Even Jump
// Difficulty: Hard
// Tags     : Array, Dynamic Programming, Stack, Sorting, Monotonic Stack, Ordered Set
// Link     : https://leetcode.com/problems/odd-even-jump/
// Runtime  : 69 ms (beats 60%)
// Memory   : 50900000 (beats 56%)
// Language : java
// Copyright: (c) 2026 gayathri16006. All rights reserved.
// Synced by: leetie
// ──────────────────────────────────────────────────

import java.util.TreeMap;

class Solution {
    public int oddEvenJumps(int[] arr) {
        int n = arr.length;
        if (n <= 1) return n;

        // odd[i] = can reach the end starting from i with an odd jump
        boolean[] odd = new boolean[n];
        // even[i] = can reach the end starting from i with an even jump
        boolean[] even = new boolean[n];

        // Base case: the last element can always reach the end
        odd[n - 1] = true;
        even[n - 1] = true;

        // Stores (value, smallest index with this value seen so far from the right)
        TreeMap<Integer, Integer> map = new TreeMap<>();
        map.put(arr[n - 1], n - 1);

        int count = 1; // n - 1 is always a good starting index

        for (int i = n - 2; i >= 0; i--) {
            // Odd jump: smallest value >= arr[i]
            var ceiling = map.ceilingEntry(arr[i]);
            if (ceiling != null) {
                odd[i] = even[ceiling.getValue()];
            }

            // Even jump: largest value <= arr[i]
            var floor = map.floorEntry(arr[i]);
            if (floor != null) {
                even[i] = odd[floor.getValue()];
            }

            if (odd[i]) {
                count++;
            }

            map.put(arr[i], i);
        }

        return count;
    }
}