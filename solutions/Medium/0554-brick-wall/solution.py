# ──────────────────────────────────────────────────
# Problem  : 554. Brick Wall
# Difficulty: Medium
# Tags     : Array, Hash Table
# Link     : https://leetcode.com/problems/brick-wall/
# Runtime  : 0 ms (beats 0%)
# Memory   : 12480000 (beats 0%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

from collections import defaultdict

class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        gap_counts = defaultdict(int)
        
        for row in wall:
            pos = 0
            # Exclude the last brick so we don't count the rightmost boundary
            for brick in row[:-1]:
                pos += brick
                gap_counts[pos] += 1
                
        # Maximum gaps aligned at any vertical line
        max_gaps = max(gap_counts.values()) if gap_counts else 0
        
        # Total rows minus the maximum aligned edges crossed
        return len(wall) - max_gaps