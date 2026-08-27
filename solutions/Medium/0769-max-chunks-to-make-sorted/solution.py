# ──────────────────────────────────────────────────
# Problem  : 769. Max Chunks To Make Sorted
# Difficulty: Medium
# Tags     : Array, Stack, Greedy, Sorting, Monotonic Stack
# Link     : https://leetcode.com/problems/max-chunks-to-make-sorted/
# Runtime  : 0 ms (beats 0%)
# Memory   : 19256000 (beats 0%)
# Language : python3
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def maxChunksToSorted(self, arr: list[int]) -> int:
        chunks = 0
        max_seen = 0
        
        for i, val in enumerate(arr):
            max_seen = max(max_seen, val)
            # Since arr is a permutation of [0, n - 1], a chunk can be formed
            # whenever the maximum value seen so far equals the current index
            if max_seen == i:
                chunks += 1
                
        return chunks