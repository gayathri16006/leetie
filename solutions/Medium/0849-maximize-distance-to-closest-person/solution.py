# ──────────────────────────────────────────────────
# Problem  : 849. Maximize Distance to Closest Person
# Difficulty: Medium
# Tags     : Array
# Link     : https://leetcode.com/problems/maximize-distance-to-closest-person/
# Runtime  : 0 ms (beats 0%)
# Memory   : 12408000 (beats 0%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        n = len(seats)
        max_dist = 0
        prev = -1

        for i in range(n):
            if seats[i] == 1:
                if prev == -1:
                    # Case 1: Leading zeros before the first person
                    max_dist = i
                else:
                    # Case 2: Zeros between two people
                    max_dist = max(max_dist, (i - prev) // 2)
                prev = i

        # Case 3: Trailing zeros after the last person
        max_dist = max(max_dist, n - 1 - prev)

        return max_dist