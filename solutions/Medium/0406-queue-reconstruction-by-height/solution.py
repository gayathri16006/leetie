# ──────────────────────────────────────────────────
# Problem  : 406. Queue Reconstruction by Height
# Difficulty: Medium
# Tags     : Array, Binary Indexed Tree, Segment Tree, Sorting
# Link     : https://leetcode.com/problems/queue-reconstruction-by-height/
# Runtime  : 0 ms (beats 0%)
# Memory   : 12264000 (beats 0%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        # Sort descending by height (h), and ascending by k
        people.sort(key=lambda x: (-x[0], x[1]))
        
        queue = []
        for p in people:
            queue.insert(p[1], p)
            
        return queue