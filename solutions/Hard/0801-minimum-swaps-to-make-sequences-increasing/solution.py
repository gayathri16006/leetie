# ──────────────────────────────────────────────────
# Problem  : 801. Minimum Swaps To Make Sequences Increasing
# Difficulty: Hard
# Tags     : Array, Dynamic Programming
# Link     : https://leetcode.com/problems/minimum-swaps-to-make-sequences-increasing/
# Runtime  : 211 ms (beats 37%)
# Memory   : 24936000 (beats 92%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):

  def minSwap(self, nums1, nums2):
    """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
    # no_swap: min swaps up to current index such that nums1[i] and nums2[i] are NOT swapped
    # swap: min swaps up to current index such that nums1[i] and nums2[i] ARE swapped
    no_swap = 0
    swap = 1

    for i in range(1, len(nums1)):
      new_no_swap = float('inf')
      new_swap = float('inf')

      # Case 1: Elements are already in strictly increasing order without swapping at index i relative to i-1
      if nums1[i] > nums1[i - 1] and nums2[i] > nums2[i - 1]:
        # Both unswapped, or both swapped
        new_no_swap = min(new_no_swap, no_swap)
        new_swap = min(new_swap, swap + 1)

      # Case 2: Cross elements are strictly increasing, allowing an alternating swap state
      if nums1[i] > nums2[i - 1] and nums2[i] > nums1[i - 1]:
        # Previous swapped & current not swapped, or previous not swapped & current swapped
        new_no_swap = min(new_no_swap, swap)
        new_swap = min(new_swap, no_swap + 1)

      no_swap, swap = new_no_swap, new_swap

    return min(no_swap, swap)