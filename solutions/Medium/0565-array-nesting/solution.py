# ──────────────────────────────────────────────────
# Problem  : 565. Array Nesting
# Difficulty: Medium
# Tags     : Array, Depth-First Search
# Link     : https://leetcode.com/problems/array-nesting/
# Runtime  : 0 ms (beats 0%)
# Memory   : 12440000 (beats 0%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def arrayNesting(self, nums):
        max_length = 0
        n = len(nums)
        
        for i in range(n):
            # If the current index has not been visited
            if nums[i] != -1:
                count = 0
                curr = i
                
                # Traverse the cycle
                while nums[curr] != -1:
                    nxt = nums[curr]
                    nums[curr] = -1  # Mark as visited
                    curr = nxt
                    count += 1
                    
                max_length = max(max_length, count)
                
        return max_length