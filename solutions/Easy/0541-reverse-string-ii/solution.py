# ──────────────────────────────────────────────────
# Problem  : 541. Reverse String II
# Difficulty: Easy
# Tags     : Two Pointers, String
# Link     : https://leetcode.com/problems/reverse-string-ii/
# Runtime  : 4 ms (beats 33%)
# Memory   : 12656000 (beats 47%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def reverseStr(self, s, k):
        chars = list(s)
        n = len(chars)
        
        for i in range(0, n, 2 * k):
            chars[i:i + k] = reversed(chars[i:i + k])
            
        return "".join(chars)