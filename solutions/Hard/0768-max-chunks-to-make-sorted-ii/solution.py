# ──────────────────────────────────────────────────
# Problem  : 768. Max Chunks To Make Sorted II
# Difficulty: Hard
# Tags     : Array, Stack, Greedy, Sorting, Monotonic Stack
# Link     : https://leetcode.com/problems/max-chunks-to-make-sorted-ii/
# Runtime  : 0 ms (beats 0%)
# Memory   : 19356000 (beats 0%)
# Language : python3
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def maxChunksToSorted(self, arr: list[int]) -> int:
        n = len(arr)
        
        # min_from_right[i] stores the minimum value in arr[i:]
        min_from_right = [0] * n
        min_from_right[-1] = arr[-1]
        for i in range(n - 2, -1, -1):
            min_from_right[i] = min(arr[i], min_from_right[i + 1])
            
        chunks = 0
        max_left = 0
        
        for i in range(n - 1):
            max_left = max(max_left, arr[i])
            # A valid chunk boundary exists if max of left part <= min of right part
            if max_left <= min_from_right[i + 1]:
                chunks += 1
                
        return chunks + 1