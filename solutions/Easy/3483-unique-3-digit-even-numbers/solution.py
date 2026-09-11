# ──────────────────────────────────────────────────
# Problem  : 3483. Unique 3-Digit Even Numbers
# Difficulty: Easy
# Tags     : Array, Hash Table, Recursion, Enumeration
# Link     : https://leetcode.com/problems/unique-3-digit-even-numbers/
# Runtime  : 1266 ms (beats 6%)
# Memory   : 12380000 (beats 60%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

from collections import Counter


class Solution(object):

  def totalNumbers(self, digits):
    """
    :type digits: List[int]
    :rtype: int
    """
    freq = Counter(digits)
    count = 0

    for num in range(100, 1000, 2):
      d1 = num // 100
      d2 = (num // 10) % 10
      d3 = num % 10

      num_freq = Counter([d1, d2, d3])

      if all(freq[d] >= num_freq[d] for d in num_freq):
        count += 1

    return count