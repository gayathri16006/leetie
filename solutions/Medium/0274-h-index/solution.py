# ──────────────────────────────────────────────────
# Problem  : 274. H-Index
# Difficulty: Medium
# Tags     : Array, Sorting, Counting Sort
# Link     : https://leetcode.com/problems/h-index/
# Runtime  : 0 ms (beats 0%)
# Memory   : 12432000 (beats 0%)
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
    citations.sort(reverse=True)

    for i, c in enumerate(citations):
      if c < i + 1:
        return i

    return len(citations)