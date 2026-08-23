# ──────────────────────────────────────────────────
# Problem  : 539. Minimum Time Difference
# Difficulty: Medium
# Tags     : Array, Math, String, Sorting
# Link     : https://leetcode.com/problems/minimum-time-difference/
# Runtime  : 4 ms (beats 96%)
# Memory   : 13960000 (beats 92%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def findMinDifference(self, timePoints):
        # 1440 minutes in a 24-hour day
        if len(timePoints) > 1440:
            return 0
        
        # Convert "HH:MM" to total minutes from 00:00
        def to_minutes(t):
            h, m = map(int, t.split(':'))
            return h * 60 + m
        
        minutes = sorted(to_minutes(t) for t in timePoints)
        
        # Initialize min_diff with the circular wrap-around difference
        # (first time + 1440) - last time
        min_diff = 1440 - minutes[-1] + minutes[0]
        
        # Check consecutive differences
        for i in range(1, len(minutes)):
            min_diff = min(min_diff, minutes[i] - minutes[i - 1])
            if min_diff == 0:
                return 0
                
        return min_diff