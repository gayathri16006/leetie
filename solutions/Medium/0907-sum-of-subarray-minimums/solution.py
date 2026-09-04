# ──────────────────────────────────────────────────
# Problem  : 907. Sum of Subarray Minimums
# Difficulty: Medium
# Tags     : Array, Dynamic Programming, Stack, Monotonic Stack
# Link     : https://leetcode.com/problems/sum-of-subarray-minimums/
# Runtime  : 846 ms (beats 45%)
# Memory   : 16488000 (beats 49%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def sumSubarrayMins(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7
        n = len(arr)

        # Distance to Previous Less Element
        left = [0] * n
        stack = []  # stores indices
        for i in range(n):
            # Strictly greater than or equal to handle duplicates correctly
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            left[i] = i - stack[-1] if stack else i + 1
            stack.append(i)

        # Distance to Next Less Element
        right = [0] * n
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            right[i] = stack[-1] - i if stack else n - i
            stack.append(i)

        # Calculate sum of contributions
        total = 0
        for i in range(n):
            total = (total + arr[i] * left[i] * right[i]) % MOD

        return total