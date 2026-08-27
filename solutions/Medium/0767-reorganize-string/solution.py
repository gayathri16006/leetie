# ──────────────────────────────────────────────────
# Problem  : 767. Reorganize String
# Difficulty: Medium
# Tags     : Hash Table, String, Greedy, Sorting, Heap (Priority Queue), Counting
# Link     : https://leetcode.com/problems/reorganize-string/
# Runtime  : 0 ms (beats 100%)
# Memory   : 19480000 (beats 54%)
# Language : python3
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

from collections import Counter
import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        counts = Counter(s)
        max_freq = max(counts.values())
        
        # If the most frequent character appears more than (n + 1) // 2 times, it's impossible
        if max_freq > (len(s) + 1) // 2:
            return ""
        
        # Max-heap storing (-count, character)
        max_heap = [(-count, char) for char, count in counts.items()]
        heapq.heapify(max_heap)
        
        result = []
        prev_count, prev_char = 0, ""
        
        while max_heap:
            count, char = heapq.heappop(max_heap)
            result.append(char)
            
            # Put the previously popped character back into the heap if it still has remaining occurrences
            if prev_count < 0:
                heapq.heappush(max_heap, (prev_count, prev_char))
                
            # Update previous character info (count is negative in max-heap)
            prev_count = count + 1
            prev_char = char
            
        return "".join(result)