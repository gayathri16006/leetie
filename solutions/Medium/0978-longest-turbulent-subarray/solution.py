# ──────────────────────────────────────────────────
# Problem  : 978. Longest Turbulent Subarray
# Difficulty: Medium
# Tags     : Array, Dynamic Programming, Sliding Window
# Link     : https://leetcode.com/problems/longest-turbulent-subarray/
# Runtime  : 58 ms (beats 70%)
# Memory   : 14948000 (beats 11%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):

  def maxTurbulenceSize(self, arr):
    """
    :type arr: List[int]
    :rtype: int
    """
    if len(arr) < 2:
      return len(arr)

    max_len = 1
    current_len = 1
    prev_cmp = 0  # 1 for greater, -1 for smaller, 0 for equal

    for i in range(1, len(arr)):
      if arr[i] > arr[i - 1]:
        curr_cmp = 1
      elif arr[i] < arr[i - 1]:
        curr_cmp = -1
      else:
        curr_cmp = 0

      if curr_cmp == 0:
        current_len = 1
      elif curr_cmp == -prev_cmp:
        current_len += 1
      else:
        current_len = 2

      prev_cmp = curr_cmp
      max_len = max(max_len, current_len)

    return max_len