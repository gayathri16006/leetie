# ──────────────────────────────────────────────────
# Problem  : 801. Minimum Swaps To Make Sequences Increasing
# Difficulty: Hard
# Tags     : Array, Dynamic Programming
# Link     : https://leetcode.com/problems/minimum-swaps-to-make-sequences-increasing/
# Runtime  : 133 ms (beats 46%)
# Memory   : 36240000 (beats 96%)
# Language : python3
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def minSwap(self, nums1: list[int], nums2: list[int]) -> int:
        n = len(nums1)
        
        # not_swap: min swaps up to index i such that nums1[i] and nums2[i] are NOT swapped
        # swap: min swaps up to index i such that nums1[i] and nums2[i] ARE swapped
        not_swap = 0
        swap = 1
        
        for i in range(1, n):
            new_not_swap = float('inf')
            new_swap = float('inf')
            
            # Case 1: Sequences are naturally increasing without changing the swap relationship
            if nums1[i] > nums1[i - 1] and nums2[i] > nums2[i - 1]:
                # Both not swapped, or both swapped
                new_not_swap = not_swap
                new_swap = swap + 1
                
            # Case 2: Sequences are increasing if we cross-swap
            if nums1[i] > nums2[i - 1] and nums2[i] > nums1[i - 1]:
                # (i-1 swapped, i not swapped) or (i-1 not swapped, i swapped)
                new_not_swap = min(new_not_swap, swap)
                new_swap = min(new_swap, not_swap + 1)
                
            not_swap = new_not_swap
            swap = new_swap
            
        return min(not_swap, swap)