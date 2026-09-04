# ──────────────────────────────────────────────────
# Problem  : 850. Rectangle Area II
# Difficulty: Hard
# Tags     : Array, Segment Tree, Sweep Line, Ordered Set
# Link     : https://leetcode.com/problems/rectangle-area-ii/
# Runtime  : 0 ms (beats 0%)
# Memory   : 12536000 (beats 0%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def rectangleArea(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: int
        """
        MOD = 10**9 + 7
        events = []

        OPEN, CLOSE = 1, -1
        for x1, y1, x2, y2 in rectangles:
            events.append((x1, OPEN, y1, y2))
            events.append((x2, CLOSE, y1, y2))

        events.sort(key=lambda e: e[0])

        active_intervals = []
        total_area = 0
        prev_x = events[0][0]

        def calculate_y_span(intervals):
            # Sort intervals by start y
            intervals.sort()
            total_y = 0
            cur_start, cur_end = -1, -1

            for y1, y2 in intervals:
                if y1 > cur_end:
                    total_y += cur_end - cur_start if cur_start != -1 else 0
                    cur_start, cur_end = y1, y2
                else:
                    cur_end = max(cur_end, y2)

            if cur_start != -1:
                total_y += cur_end - cur_start

            return total_y

        for x, event_type, y1, y2 in events:
            # Add area for the delta x
            if x > prev_x:
                total_area = (total_area + (x - prev_x) * calculate_y_span(active_intervals)) % MOD
                prev_x = x

            # Update active intervals
            if event_type == OPEN:
                active_intervals.append((y1, y2))
            else:
                active_intervals.remove((y1, y2))

        return total_area