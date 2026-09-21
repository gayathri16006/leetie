// ──────────────────────────────────────────────────
// Problem  : 1012. Numbers With Repeated Digits
// Difficulty: Hard
// Tags     : Math, Dynamic Programming
// Link     : https://leetcode.com/problems/numbers-with-repeated-digits/
// Runtime  : 0 ms (beats 0%)
// Memory   : 42040000 (beats 0%)
// Language : java
// Copyright: (c) 2026 gayathri16006. All rights reserved.
// Synced by: leetie
// ──────────────────────────────────────────────────

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

class Solution {
    public int numDupDigitsAtMostN(int n) {
        return n - countSpecialNumbers(n);
    }

    private int countSpecialNumbers(int n) {
        List<Integer> digits = new ArrayList<>();
        for (int temp = n; temp > 0; temp /= 10) {
            digits.add(0, temp % 10);
        }

        int len = digits.size();
        int count = 0;

        // 1. Numbers with fewer digits than n
        for (int i = 1; i < len; i++) {
            count += 9 * permutation(9, i - 1);
        }

        // 2. Numbers with the same length as n
        Set<Integer> seen = new HashSet<>();
        for (int i = 0; i < len; i++) {
            int currentDigit = digits.get(i);
            int startDigit = (i == 0) ? 1 : 0;

            for (int d = startDigit; d < currentDigit; d++) {
                if (!seen.contains(d)) {
                    count += permutation(10 - (i + 1), len - 1 - i);
                }
            }

            // If the current digit was already used in the prefix, stop
            if (seen.contains(currentDigit)) {
                break;
            }

            seen.add(currentDigit);

            // If we reached the end with all unique digits, count n itself
            if (i == len - 1) {
                count++;
            }
        }

        return count;
    }

    // Calculates P(m, n) = m! / (m - n)!
    private int permutation(int m, int n) {
        int result = 1;
        for (int i = 0; i < n; i++) {
            result *= (m - i);
        }
        return result;
    }
}