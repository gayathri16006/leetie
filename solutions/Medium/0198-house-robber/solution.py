# ──────────────────────────────────────────────────
# Problem  : 198. House Robber
# Difficulty: Medium
# Tags     : Array, Dynamic Programming
# Link     : https://leetcode.com/problems/house-robber/
# Runtime  : 0 ms (beats 0%)
# Memory   : 12336000 (beats 0%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):

  def rob(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    rob1, rob2 = 0, 0

    # [rob1, rob2, num, num+1, ...]
    for num in nums:
      # Max loot if we rob the current house vs if we skip it
      current = max(rob1 + num, rob2)
      rob1 = rob2
      rob2 = current

    return rob2