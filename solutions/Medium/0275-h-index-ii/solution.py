# ──────────────────────────────────────────────────
# Problem  : 275. H-Index II
# Difficulty: Medium
# Tags     : Array, Binary Search
# Link     : https://leetcode.com/problems/h-index-ii/
# Runtime  : 0 ms (beats 0%)
# Memory   : 12328000 (beats 0%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):

  def hIndex(self, citations):
    """
    :type citations: List[int]
    :rtype: int
    """
    n = len(citations)
    left, right = 0, n - 1

    while left <= right:
      mid = left + (right - left) // 2
      # Number of papers with citations >= citations[mid]
      h = n - mid

      if citations[mid] == h:
        return h
      elif citations[mid] < h:
        left = mid + 1
      else:
        right = mid - 1

    # The maximum h-index will be n - left
    return n - left