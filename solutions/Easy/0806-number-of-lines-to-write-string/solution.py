# ──────────────────────────────────────────────────
# Problem  : 806. Number of Lines To Write String
# Difficulty: Easy
# Tags     : Array, String
# Link     : https://leetcode.com/problems/number-of-lines-to-write-string/
# Runtime  : 27 ms (beats 7%)
# Memory   : 12408000 (beats 31%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def numberOfLines(self, widths, s):
        """
        :type widths: List[int]
        :type s: str
        :rtype: List[int]
        """
        lines = 1
        current_width = 0
        
        for ch in s:
            w = widths[ord(ch) - ord('a')]
            if current_width + w > 100:
                lines += 1
                current_width = w
            else:
                current_width += w
                
        return [lines, current_width]