# ──────────────────────────────────────────────────
# Problem  : 729. My Calendar I
# Difficulty: Medium
# Tags     : Array, Binary Search, Design, Segment Tree, Ordered Set
# Link     : https://leetcode.com/problems/my-calendar-i/
# Runtime  : 19 ms (beats 98%)
# Memory   : 20312000 (beats 6%)
# Language : python3
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

import bisect

class MyCalendar:

    def __init__(self):
        # Keeps sorted list of (start, end) intervals
        self.calendar = []

    def book(self, startTime: int, endTime: int) -> bool:
        # Binary search for the position to insert (startTime, endTime)
        idx = bisect.bisect_right(self.calendar, (startTime, endTime))
        
        # Check conflict with the previous event: prev_end > startTime
        if idx > 0 and self.calendar[idx - 1][1] > startTime:
            return False
            
        # Check conflict with the next event: endTime > next_start
        if idx < len(self.calendar) and endTime > self.calendar[idx][0]:
            return False
            
        self.calendar.insert(idx, (startTime, endTime))
        return True