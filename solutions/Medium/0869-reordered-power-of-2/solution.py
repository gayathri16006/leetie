# ──────────────────────────────────────────────────
# Problem  : 869. Reordered Power of 2
# Difficulty: Medium
# Tags     : Hash Table, Math, Sorting, Counting, Enumeration
# Link     : https://leetcode.com/problems/reordered-power-of-2/
# Runtime  : 0 ms (beats 100%)
# Memory   : 12352000 (beats 57%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def reorderedPowerOf2(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # A helper to get the sorted digit signature of an integer
        def digit_signature(x):
            return sorted(str(x))

        target = digit_signature(n)

        # Check all powers of 2 up to 10^9 (2^0 to 2^29)
        return any(digit_signature(1 << i) == target for i in range(30))