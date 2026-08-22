# ──────────────────────────────────────────────────
# Problem  : 481. Magical String
# Difficulty: Medium
# Tags     : Two Pointers, String
# Link     : https://leetcode.com/problems/magical-string/
# Runtime  : 65 ms (beats 76%)
# Memory   : 13700000 (beats 22%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def magicalString(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        if n <= 3:
            return 1

        # Seed with the first few known characters "122"
        s = [1, 2, 2]
        
        # Pointer indicating the run length of the next group
        head = 2

        while len(s) < n:
            # Alternate between 1 and 2: if last is 1, next is 2; if last is 2, next is 1
            next_num = 3 - s[-1]
            count = s[head]
            
            # Append next_num 'count' times
            s.extend([next_num] * count)
            head += 1

        # Count occurrences of 1 in the first n digits
        return s[:n].count(1)