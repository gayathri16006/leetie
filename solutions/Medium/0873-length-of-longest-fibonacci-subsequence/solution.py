# ──────────────────────────────────────────────────
# Problem  : 873. Length of Longest Fibonacci Subsequence
# Difficulty: Medium
# Tags     : Array, Hash Table, Dynamic Programming
# Link     : https://leetcode.com/problems/length-of-longest-fibonacci-subsequence/
# Runtime  : 0 ms (beats 0%)
# Memory   : 12356000 (beats 0%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def lenLongestFibSubseq(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        index_map = {val: i for i, val in enumerate(arr)}
        dp = {}
        max_len = 0
        n = len(arr)

        for k in range(n):
            for j in range(k):
                target = arr[k] - arr[j]
                # target must precede arr[j]
                if target < arr[j] and target in index_map:
                    i = index_map[target]
                    length = dp.get((i, j), 2) + 1
                    dp[(j, k)] = length
                    if length > max_len:
                        max_len = length

        return max_len if max_len >= 3 else 0