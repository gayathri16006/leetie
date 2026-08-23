# ──────────────────────────────────────────────────
# Problem  : 560. Subarray Sum Equals K
# Difficulty: Medium
# Tags     : Array, Hash Table, Prefix Sum
# Link     : https://leetcode.com/problems/subarray-sum-equals-k/
# Runtime  : 41 ms (beats 39%)
# Memory   : 14584000 (beats 96%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

from collections import defaultdict

class Solution(object):
    def subarraySum(self, nums, k):
        # Map prefix_sum -> count of occurrences
        # Base case: prefix sum 0 occurs once before iterating (empty prefix)
        prefix_counts = defaultdict(int)
        prefix_counts[0] = 1
        
        running_sum = 0
        total_subarrays = 0
        
        for num in nums:
            running_sum += num
            
            # If (running_sum - k) exists in prefix_counts, add its frequency
            if running_sum - k in prefix_counts:
                total_subarrays += prefix_counts[running_sum - k]
                
            # Record current running_sum in the map
            prefix_counts[running_sum] += 1
            
        return total_subarrays