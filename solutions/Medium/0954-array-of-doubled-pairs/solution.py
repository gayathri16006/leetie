# ──────────────────────────────────────────────────
# Problem  : 954. Array of Doubled Pairs
# Difficulty: Medium
# Tags     : Array, Hash Table, Greedy, Sorting
# Link     : https://leetcode.com/problems/array-of-doubled-pairs/
# Runtime  : 67 ms (beats 83%)
# Memory   : 14092000 (beats 54%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

from collections import Counter

class Solution(object):
    def canReorderDoubled(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        count = Counter(arr)
        
        
        for x in sorted(count.keys(), key=abs):
            if count[x] > count[2 * x]:
                return False
            count[2 * x] -= count[x]
            
        return True