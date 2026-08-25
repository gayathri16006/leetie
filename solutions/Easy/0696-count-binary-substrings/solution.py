# ──────────────────────────────────────────────────
# Problem  : 696. Count Binary Substrings
# Difficulty: Easy
# Tags     : Two Pointers, String
# Link     : https://leetcode.com/problems/count-binary-substrings/
# Runtime  : 55 ms (beats 60%)
# Memory   : 19552000 (beats 64%)
# Language : python3
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        ans = 0
        prev_run = 0
        curr_run = 1
        
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                curr_run += 1
            else:
                ans += min(prev_run, curr_run)
                prev_run = curr_run
                curr_run = 1
                
        # Add the valid substrings formed by the last two groups
        ans += min(prev_run, curr_run)
        
        return ans