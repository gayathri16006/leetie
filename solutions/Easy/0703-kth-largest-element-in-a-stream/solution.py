# ──────────────────────────────────────────────────
# Problem  : 703. Kth Largest Element in a Stream
# Difficulty: Easy
# Tags     : Tree, Design, Binary Search Tree, Heap (Priority Queue), Binary Tree, Data Stream
# Link     : https://leetcode.com/problems/kth-largest-element-in-a-stream/
# Runtime  : 13 ms (beats 77%)
# Memory   : 25852000 (beats 9%)
# Language : python3
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

import heapq
from typing import List

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.min_heap = []
        
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        if len(self.min_heap) < self.k:
            heapq.heappush(self.min_heap, val)
        elif val > self.min_heap[0]:
            heapq.heapreplace(self.min_heap, val)
            
        # The root of the min-heap represents the k-th largest element
        return self.min_heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)