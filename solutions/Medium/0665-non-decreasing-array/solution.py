# ──────────────────────────────────────────────────
# Problem  : 665. Non-decreasing Array
# Difficulty: Medium
# Tags     : Array
# Link     : https://leetcode.com/problems/non-decreasing-array/
# Runtime  : 0 ms (beats 100%)
# Memory   : 20520000 (beats 45%)
# Language : python3
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

from typing import List

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        modified = False
        
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                if modified:
                    return False
                
                # Check if lowering nums[i] to nums[i + 1] maintains non-decreasing order
                if i == 0 or nums[i - 1] <= nums[i + 1]:
                    nums[i] = nums[i + 1]
                else:
                    # Otherwise, raise nums[i + 1] to nums[i]
                    nums[i + 1] = nums[i]
                    
                modified = True
                
        return True