# ──────────────────────────────────────────────────
# Problem  : 1520. Maximum Number of Non-Overlapping Substrings
# Difficulty: Hard
# Tags     : Hash Table, String, Greedy, Sorting
# Link     : https://leetcode.com/problems/maximum-number-of-non-overlapping-substrings/
# Runtime  : 239 ms (beats 97%)
# Memory   : 13548000 (beats 32%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def maxNumOfSubstrings(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        first = {}
        last = {}
        
        for i, ch in enumerate(s):
            if ch not in first:
                first[ch] = i
            last[ch] = i
            
        intervals = []
        
        for ch in first:
            l = first[ch]
            r = last[ch]
            valid = True
            
            # Expand the interval to cover all characters inside it
            k = l
            while k <= r:
                c = s[k]
                if first[c] < l:
                    valid = False
                    break
                r = max(r, last[c])
                k += 1
                
            if valid:
                intervals.append((r, l))  # Store as (end, start) for easy sorting
                
        intervals.sort()
        
        res = []
        prev_end = -1
        
        for r, l in intervals:
            if l > prev_end:
                res.append(s[l:r + 1])
                prev_end = r
                
        return res