# ──────────────────────────────────────────────────
# Problem  : 540. Single Element in a Sorted Array
# Difficulty: Medium
# Tags     : Array, Binary Search
# Link     : https://leetcode.com/problems/single-element-in-a-sorted-array/
# Runtime  : 0 ms (beats 0%)
# Memory   : 12576000 (beats 0%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def singleNonDuplicate(self, nums):
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = left + (right - left) // 2
            
            # Check if mid matches its corresponding pair partner
            # If mid is even -> mid ^ 1 is mid + 1
            # If mid is odd  -> mid ^ 1 is mid - 1
            if nums[mid] == nums[mid ^ 1]:
                # Pattern is normal, single element is to the right
                left = mid + 1
            else:
                # Pattern is broken, single element is at mid or to the left
                right = mid
                
        return nums[left]