# ──────────────────────────────────────────────────
# Problem  : 632. Smallest Range Covering Elements from K Lists
# Difficulty: Hard
# Tags     : Array, Hash Table, Greedy, Sliding Window, Sorting, Heap (Priority Queue)
# Link     : https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/
# Runtime  : 449 ms (beats 70%)
# Memory   : 27352000 (beats 33%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

import heapq

class Solution(object):
    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        min_heap = []
        cur_max = float('-inf')
        
        # Initialize heap with the first element of each list
        for i in range(len(nums)):
            heapq.heappush(min_heap, (nums[i][0], i, 0))
            cur_max = max(cur_max, nums[i][0])
            
        best_range = [float('-inf'), float('inf')]
        
        while min_heap:
            cur_min, list_idx, elem_idx = heapq.heappop(min_heap)
            
            # Update best range if current window [cur_min, cur_max] is smaller
            if cur_max - cur_min < best_range[1] - best_range[0]:
                best_range = [cur_min, cur_max]
                
            # If any list is exhausted, we cannot form a valid range covering all lists anymore
            if elem_idx + 1 == len(nums[list_idx]):
                break
                
            # Push the next element from the current list into the heap
            next_val = nums[list_idx][elem_idx + 1]
            heapq.heappush(min_heap, (next_val, list_idx, elem_idx + 1))
            cur_max = max(cur_max, next_val)
            
        return best_range