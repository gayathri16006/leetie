# ──────────────────────────────────────────────────
# Problem  : 689. Maximum Sum of 3 Non-Overlapping Subarrays
# Difficulty: Hard
# Tags     : Array, Dynamic Programming, Sliding Window, Prefix Sum
# Link     : https://leetcode.com/problems/maximum-sum-of-3-non-overlapping-subarrays/
# Runtime  : 24 ms (beats 65%)
# Memory   : 22128000 (beats 69%)
# Language : python3
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

from typing import List

class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        
        # 1. Compute sliding window sums of size k
        w = [0] * (n - k + 1)
        curr_sum = sum(nums[:k])
        w[0] = curr_sum
        for i in range(1, len(w)):
            curr_sum += nums[i + k - 1] - nums[i - 1]
            w[i] = curr_sum
            
        m = len(w)
        
        # 2. left[i]: Best starting index for an interval in w[0...i]
        left = [0] * m
        best_left = 0
        for i in range(m):
            if w[i] > w[best_left]:
                best_left = i
            left[i] = best_left
            
        # 3. right[i]: Best starting index for an interval in w[i...m-1]
        right = [0] * m
        best_right = m - 1
        for i in range(m - 1, -1, -1):
            if w[i] >= w[best_right]:  # '>=' ensures lexicographically smallest index
                best_right = i
            right[i] = best_right
            
        # 4. Iterate over middle interval starting index j (from k to m - 1 - k)
        max_total = 0
        ans = []
        for j in range(k, m - k):
            l = left[j - k]
            r = right[j + k]
            total = w[l] + w[j] + w[r]
            
            if total > max_total:
                max_total = total
                ans = [l, j, r]
                
        return ans