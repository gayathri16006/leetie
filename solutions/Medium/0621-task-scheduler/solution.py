# ──────────────────────────────────────────────────
# Problem  : 621. Task Scheduler
# Difficulty: Medium
# Tags     : Array, Hash Table, Greedy, Sorting, Heap (Priority Queue), Counting
# Link     : https://leetcode.com/problems/task-scheduler/
# Runtime  : 0 ms (beats 0%)
# Memory   : 19532000 (beats 0%)
# Language : python3
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

from collections import Counter
from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        max_freq = max(freq.values())
        
        # Count how many tasks share the maximum frequency
        max_count = sum(1 for count in freq.values() if count == max_freq)
        
        # Calculate intervals using the math formula
        intervals = (max_freq - 1) * (n + 1) + max_count
        
        # Result cannot be shorter than the total number of tasks
        return max(len(tasks), intervals)