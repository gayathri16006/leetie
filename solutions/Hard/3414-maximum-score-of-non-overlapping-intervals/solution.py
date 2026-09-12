# ──────────────────────────────────────────────────
# Problem  : 3414. Maximum Score of Non-overlapping Intervals
# Difficulty: Hard
# Tags     : Array, Binary Search, Dynamic Programming, Sorting
# Link     : https://leetcode.com/problems/maximum-score-of-non-overlapping-intervals/
# Runtime  : 1697 ms (beats 100%)
# Memory   : 71772000 (beats 100%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

from bisect import bisect_left

class Solution(object):
    def maximumWeight(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[int]
        """
        # Store as (l, r, weight, original_index)
        arr = sorted(
            [(iv[0], iv[1], iv[2], i) for i, iv in enumerate(intervals)],
            key=lambda x: x[1]
        )
        
        n = len(arr)
        ends = [x[1] for x in arr]
        
        # dp[k][i] stores (negative_weight, indices_tuple)
        # using k intervals chosen from the first i intervals.
        dp = [[(0, ())] * (n + 1) for _ in range(5)]
        
        for i in range(1, n + 1):
            l, r, w, orig_idx = arr[i - 1]
            # Find the largest j such that ends[j - 1] < l
            j = bisect_left(ends, l)
            
            for k in range(1, 5):
                # Option 1: Do not pick the current interval
                best = dp[k][i - 1]
                
                # Option 2: Pick the current interval
                prev_neg_w, prev_indices = dp[k - 1][j]
                if k == 1 or prev_indices or prev_neg_w < 0:
                    cand_neg_w = prev_neg_w - w
                    cand_indices = tuple(sorted(prev_indices + (orig_idx,)))
                    cand = (cand_neg_w, cand_indices)
                    
                    if cand < best:
                        best = cand
                        
                dp[k][i] = best
                
        # Find the overall best result across all counts 1 <= k <= 4
        best_state = (0, ())
        for k in range(1, 5):
            if dp[k][n][0] < 0 and dp[k][n] < best_state:
                best_state = dp[k][n]
                
        return list(best_state[1])