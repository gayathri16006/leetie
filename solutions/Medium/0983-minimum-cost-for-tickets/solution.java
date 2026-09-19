// ──────────────────────────────────────────────────
// Problem  : 983. Minimum Cost For Tickets
// Difficulty: Medium
// Tags     : Array, Dynamic Programming
// Link     : https://leetcode.com/problems/minimum-cost-for-tickets/
// Runtime  : 0 ms (beats 0%)
// Memory   : 42844000 (beats 0%)
// Language : java
// Copyright: (c) 2026 gayathri16006. All rights reserved.
// Synced by: leetie
// ──────────────────────────────────────────────────

import java.util.HashSet;
import java.util.Set;

class Solution {
    public int mincostTickets(int[] days, int[] costs) {
        // Store travel days in a set for O(1) lookup
        Set<Integer> travelDays = new HashSet<>();
        for (int day : days) {
            travelDays.add(day);
        }

        int lastDay = days[days.length - 1];
        // dp[i] represents the minimum cost to travel up to day i
        int[] dp = new int[lastDay + 1];

        for (int i = 1; i <= lastDay; i++) {
            if (!travelDays.contains(i)) {
                // If not traveling on day i, cost remains the same as day i - 1
                dp[i] = dp[i - 1];
            } else {
                // Buy 1-day pass, 7-day pass, or 30-day pass
                int cost1 = dp[Math.max(0, i - 1)] + costs[0];
                int cost7 = dp[Math.max(0, i - 7)] + costs[1];
                int cost30 = dp[Math.max(0, i - 30)] + costs[2];

                dp[i] = Math.min(cost1, Math.min(cost7, cost30));
            }
        }

        return dp[lastDay];
    }
}