# ──────────────────────────────────────────────────
# Problem  : 480. Sliding Window Median
# Difficulty: Hard
# Tags     : Array, Hash Table, Sliding Window, Heap (Priority Queue), Treap
# Link     : https://leetcode.com/problems/sliding-window-median/
# Runtime  : 475 ms (beats 38%)
# Memory   : 22488000 (beats 83%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

import bisect

class Solution(object):
    def medianSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """
        window = sorted(nums[:k])
        medians = []
        
        def get_median():
            if k % 2 == 1:
                return float(window[k // 2])
            else:
                return (window[k // 2 - 1] + window[k // 2]) / 2.0

        medians.append(get_median())

        for i in range(k, len(nums)):
            # Remove the element falling out of the sliding window
            outgoing_val = nums[i - k]
            idx_to_remove = bisect.bisect_left(window, outgoing_val)
            window.pop(idx_to_remove)

            # Insert the new incoming element in sorted order
            incoming_val = nums[i]
            bisect.insort(window, incoming_val)

            medians.append(get_median())

        return medians