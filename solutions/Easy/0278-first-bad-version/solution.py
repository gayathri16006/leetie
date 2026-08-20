# ──────────────────────────────────────────────────
# Problem  : 278. First Bad Version
# Difficulty: Easy
# Tags     : Binary Search, Interactive
# Link     : https://leetcode.com/problems/first-bad-version/
# Runtime  : 15 ms (beats 0%)
# Memory   : 12140000 (beats 0%)
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
        # The first bad version is at `mid` or to the left
        right = mid
      else:
        # The first bad version must be to the right of `mid`
        left = mid + 1

    return left