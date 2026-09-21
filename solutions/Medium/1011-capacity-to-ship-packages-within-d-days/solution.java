// ──────────────────────────────────────────────────
// Problem  : 1011. Capacity To Ship Packages Within D Days
// Difficulty: Medium
// Tags     : Array, Binary Search
// Link     : https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/
// Runtime  : 0 ms (beats 0%)
// Memory   : 42716000 (beats 0%)
// Language : java
// Copyright: (c) 2026 gayathri16006. All rights reserved.
// Synced by: leetie
// ──────────────────────────────────────────────────

class Solution {
    public int shipWithinDays(int[] weights, int days) {
        int left = 0;
        int right = 0;

        for (int w : weights) {
            left = Math.max(left, w);
            right += w;
        }

        while (left < right) {
            int mid = left + (right - left) / 2;

            if (canShip(weights, days, mid)) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }

        return left;
    }

    private boolean canShip(int[] weights, int days, int capacity) {
        int requiredDays = 1;
        int currentWeight = 0;

        for (int w : weights) {
            if (currentWeight + w > capacity) {
                requiredDays++;
                currentWeight = 0;
            }
            currentWeight += w;
        }

        return requiredDays <= days;
    }
}