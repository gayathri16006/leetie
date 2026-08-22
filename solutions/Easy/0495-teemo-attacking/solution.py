# ──────────────────────────────────────────────────
# Problem  : 495. Teemo Attacking
# Difficulty: Easy
# Tags     : Array, Simulation
# Link     : https://leetcode.com/problems/teemo-attacking/
# Runtime  : 22 ms (beats 49%)
# Memory   : 13200000 (beats 49%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        if not timeSeries or duration == 0:
            return 0

        total_time = 0
        for i in range(len(timeSeries) - 1):
            total_time += min(duration, timeSeries[i + 1] - timeSeries[i])
        
        return total_time + duration