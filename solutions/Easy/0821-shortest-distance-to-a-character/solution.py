# ──────────────────────────────────────────────────
# Problem  : 821. Shortest Distance to a Character
# Difficulty: Easy
# Tags     : Array, Two Pointers, String
# Link     : https://leetcode.com/problems/shortest-distance-to-a-character/
# Runtime  : 0 ms (beats 0%)
# Memory   : 12360000 (beats 0%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def shortestToChar(self, s, c):
        """
        :type s: str
        :type c: str
        :rtype: List[int]
        """
        n = len(s)
        ans = [0] * n

        # Left-to-right pass
        prev = -float('inf')
        for i in range(n):
            if s[i] == c:
                prev = i
            ans[i] = i - prev

        # Right-to-left pass
        prev = float('inf')
        for i in range(n - 1, -1, -1):
            if s[i] == c:
                prev = i
            ans[i] = min(ans[i], prev - i)

        return ans