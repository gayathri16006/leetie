# ──────────────────────────────────────────────────
# Problem  : 830. Positions of Large Groups
# Difficulty: Easy
# Tags     : String
# Link     : https://leetcode.com/problems/positions-of-large-groups/
# Runtime  : 0 ms (beats 0%)
# Memory   : 12460000 (beats 0%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def largeGroupPositions(self, s):
        """
        :type s: str
        :rtype: List[List[int]]
        """
        ans = []
        start = 0
        n = len(s)

        for end in range(n):
            # Check if we reached the end of the string or the character changes
            if end == n - 1 or s[end] != s[end + 1]:
                if end - start + 1 >= 3:
                    ans.append([start, end])
                start = end + 1

        return ans