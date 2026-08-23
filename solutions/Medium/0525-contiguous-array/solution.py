# ──────────────────────────────────────────────────
# Problem  : 525. Contiguous Array
# Difficulty: Medium
# Tags     : Array, Hash Table, Prefix Sum
# Link     : https://leetcode.com/problems/contiguous-array/
# Runtime  : 0 ms (beats 0%)
# Memory   : 12588000 (beats 0%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def findMaxLength(self, nums):
        # Map running_sum -> earliest index seen
        # Base case: sum 0 at index -1
        sum_indices = {0: -1}
        running_sum = 0
        max_length = 0
        
        for i, num in enumerate(nums):
            # Treat 1 as +1, 0 as -1
            running_sum += 1 if num == 1 else -1
            
            if running_sum in sum_indices:
                max_length = max(max_length, i - sum_indices[running_sum])
            else:
                # Store only the first occurrence to maximize subarray length
                sum_indices[running_sum] = i
                
        return max_length