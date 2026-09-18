# ──────────────────────────────────────────────────
# Problem  : 942. DI String Match
# Difficulty: Easy
# Tags     : Array, Two Pointers, String, Greedy
# Link     : https://leetcode.com/problems/di-string-match/
# Runtime  : 7 ms (beats 38%)
# Memory   : 13436000 (beats 90%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def diStringMatch(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        low = 0
        high = len(s)
        ans = []
        
        for ch in s:
            if ch == 'I':
                ans.append(low)
                low += 1
            else:
                ans.append(high)
                high -= 1
                
        ans.append(low)
        return ans