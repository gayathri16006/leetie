# ──────────────────────────────────────────────────
# Problem  : 624. Maximum Distance in Arrays
# Difficulty: Medium
# Tags     : Array, Greedy
# Link     : https://leetcode.com/problems/maximum-distance-in-arrays/
# Runtime  : 69 ms (beats 75%)
# Memory   : 30952000 (beats 43%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def maxDistance(self, arrays):
        max_dist = 0
        
        # Initialize with the min and max of the first array
        min_val = arrays[0][0]
        max_val = arrays[0][-1]
        
        # Iterate through the remaining arrays
        for i in range(1, len(arrays)):
            curr_arr = arrays[i]
            
            # Calculate distances using the previous min/max to ensure different arrays
            max_dist = max(
                max_dist,
                abs(curr_arr[-1] - min_val),
                abs(max_val - curr_arr[0])
            )
            
            # Update running min and max
            min_val = min(min_val, curr_arr[0])
            max_val = max(max_val, curr_arr[-1])
            
        return max_dist