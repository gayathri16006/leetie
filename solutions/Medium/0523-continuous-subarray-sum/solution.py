# ──────────────────────────────────────────────────
# Problem  : 523. Continuous Subarray Sum
# Difficulty: Medium
# Tags     : Array, Hash Table, Math, Prefix Sum, Pigeonhole Principle
# Link     : https://leetcode.com/problems/continuous-subarray-sum/
# Runtime  : 44 ms (beats 95%)
# Memory   : 31160000 (beats 85%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def checkSubarraySum(self, nums, k):
        # Map remainder to the earliest index it was observed
        # Base case: remainder 0 at index -1 to handle valid subarrays starting at index 0
        remainder_map = {0: -1}
        running_sum = 0
        
        for i, num in enumerate(nums):
            running_sum += num
            remainder = running_sum % k
            
            if remainder in remainder_map:
                # Check if subarray length is at least 2
                if i - remainder_map[remainder] >= 2:
                    return True
            else:
                # Only store the earliest index to maximize the subarray length
                remainder_map[remainder] = i
                
        return False