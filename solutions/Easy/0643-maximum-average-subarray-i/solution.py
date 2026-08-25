# ──────────────────────────────────────────────────
# Problem  : 643. Maximum Average Subarray I
# Difficulty: Easy
# Tags     : Array, Sliding Window
# Link     : https://leetcode.com/problems/maximum-average-subarray-i/
# Runtime  : 42 ms (beats 97%)
# Memory   : 29200000 (beats 50%)
# Language : python3
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # Calculate the sum of the first window of size k
        current_sum = sum(nums[:k])
        max_sum = current_sum
        
        # Slide the window across the rest of the array
        for i in range(k, len(nums)):
            current_sum += nums[i] - nums[i - k]
            if current_sum > max_sum:
                max_sum = current_sum
                
        return max_sum / k