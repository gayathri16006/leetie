# ──────────────────────────────────────────────────
# Problem  : 630. Course Schedule III
# Difficulty: Hard
# Tags     : Array, Greedy, Sorting, Heap (Priority Queue)
# Link     : https://leetcode.com/problems/course-schedule-iii/
# Runtime  : 77 ms (beats 95%)
# Memory   : 16268000 (beats 50%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

import heapq

class Solution(object):
    def scheduleCourse(self, courses):
        """
        :type courses: List[List[int]]
        :rtype: int
        """
        # Sort courses by their deadlines (lastDay) in ascending order
        courses.sort(key=lambda x: x[1])
        
        max_heap = []  # Store durations as negative values for max-heap behavior
        total_time = 0
        
        for duration, last_day in courses:
            # If the course can be taken within its deadline, add it
            if total_time + duration <= last_day:
                total_time += duration
                heapq.heappush(max_heap, -duration)
            # Otherwise, check if replacing a previous longer course saves time
            elif max_heap and -max_heap[0] > duration:
                total_time += heapq.heappop(max_heap) + duration  # subtract largest duration, add current
                heapq.heappush(max_heap, -duration)
                
        return len(max_heap)