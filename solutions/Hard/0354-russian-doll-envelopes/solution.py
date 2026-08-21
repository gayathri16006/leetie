# ──────────────────────────────────────────────────
# Problem  : 354. Russian Doll Envelopes
# Difficulty: Hard
# Tags     : Array, Binary Search, Dynamic Programming, Sorting, Longest Increasing Subsequence
# Link     : https://leetcode.com/problems/russian-doll-envelopes/
# Runtime  : 258 ms (beats 52%)
# Memory   : 50636000 (beats 66%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

import bisect

class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        if not envelopes:
            return 0
        
        # Sort width ascending; if widths are equal, sort height descending
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        
        # Find the LIS on the heights
        lis = []
        for _, h in envelopes:
            idx = bisect.bisect_left(lis, h)
            if idx == len(lis):
                lis.append(h)
            else:
                lis[idx] = h
                
        return len(lis)