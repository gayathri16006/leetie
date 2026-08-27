# ──────────────────────────────────────────────────
# Problem  : 731. My Calendar II
# Difficulty: Medium
# Tags     : Array, Binary Search, Design, Segment Tree, Prefix Sum, Ordered Set
# Link     : https://leetcode.com/problems/my-calendar-ii/
# Runtime  : 335 ms (beats 61%)
# Memory   : 20080000 (beats 75%)
# Language : python3
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class MyCalendarTwo:

    def __init__(self):
        # List of all single booked intervals
        self.bookings = []
        # List of overlapped intervals (double booked)
        self.double_bookings = []

    def book(self, startTime: int, endTime: int) -> bool:
        # Check if new interval intersects with any existing double-booked intervals
        for s, e in self.double_bookings:
            if max(startTime, s) < min(endTime, e):
                return False

        # Find overlaps with single bookings and record them in double_bookings
        for s, e in self.bookings:
            if max(startTime, s) < min(endTime, e):
                self.double_bookings.append((max(startTime, s), min(endTime, e)))

        self.bookings.append((startTime, endTime))
        return True