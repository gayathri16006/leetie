# ──────────────────────────────────────────────────
# Problem  : 732. My Calendar III
# Difficulty: Hard
# Tags     : Binary Search, Design, Segment Tree, Prefix Sum, Ordered Set
# Link     : https://leetcode.com/problems/my-calendar-iii/
# Runtime  : 0 ms (beats 0%)
# Memory   : 19232000 (beats 0%)
# Language : python3
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

from sortedcontainers import SortedDict

class MyCalendarThree:

    def __init__(self):
        # Maps time point -> net change in active bookings
        self.timeline = SortedDict()

    def book(self, startTime: int, endTime: int) -> int:
        # Increment active event count at start, decrement at end
        self.timeline[startTime] = self.timeline.get(startTime, 0) + 1
        self.timeline[endTime] = self.timeline.get(endTime, 0) - 1

        max_k = 0
        ongoing = 0
        
        # Sweep-line across sorted boundary points
        for delta in self.timeline.values():
            ongoing += delta
            if ongoing > max_k:
                max_k = ongoing

        return max_k