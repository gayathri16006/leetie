# ──────────────────────────────────────────────────
# Problem  : 278. First Bad Version
# Difficulty: Easy
# Tags     : Binary Search, Interactive
# Link     : https://leetcode.com/problems/first-bad-version/
# Runtime  : 11 ms (beats 85%)
# Memory   : 12160000 (beats 99%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):


class Solution(object):

  def firstBadVersion(self, n):
    """
    :type n: int
    :rtype: int
    """
    left, right = 1, n

    while left < right:
      mid = left + (right - left) // 2
      if isBadVersion(mid):
        right = mid
      else:
        left = mid + 1

    return left