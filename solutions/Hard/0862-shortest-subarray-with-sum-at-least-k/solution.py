# ──────────────────────────────────────────────────
# Problem  : 862. Shortest Subarray with Sum at Least K
# Difficulty: Hard
# Tags     : Array, Binary Search, Queue, Sliding Window, Heap (Priority Queue), Prefix Sum, Monotonic Queue
# Link     : https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/
# Runtime  : 171 ms (beats 64%)
# Memory   : 17656000 (beats 54%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

from collections import deque

class Solution(object):
    def shortestSubarray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        # Compute prefix sums
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        q = deque()
        min_len = float('inf')

        for i in range(n + 1):
            # Check if we found a valid window
            while q and prefix[i] - prefix[q[0]] >= k:
                min_len = min(min_len, i - q.popleft())

            # Maintain monotonic increasing order of prefix sums
            while q and prefix[i] <= prefix[q[-1]]:
                q.pop()

            q.append(i)

        return min_len if min_len != float('inf') else -1