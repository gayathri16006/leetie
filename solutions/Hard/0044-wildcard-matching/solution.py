# ──────────────────────────────────────────────────
# Problem  : 44. Wildcard Matching
# Difficulty: Hard
# Tags     : String, Dynamic Programming, Greedy, Recursion
# Link     : https://leetcode.com/problems/wildcard-matching/
# Runtime  : 8 ms (beats 84%)
# Memory   : 12376000 (beats 79%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        s_idx, p_idx = 0, 0
        star_idx = -1
        match_idx = 0
        
        while s_idx < len(s):
            # 1. Characters match directly or '?' matches any single character
            if p_idx < len(p) and (p[p_idx] == s[s_idx] or p[p_idx] == '?'):
                s_idx += 1
                p_idx += 1
            # 2. '*' found: record star position and assume it matches 0 characters first
            elif p_idx < len(p) and p[p_idx] == '*':
                star_idx = p_idx
                match_idx = s_idx
                p_idx += 1
            # 3. Mismatch occurs, but a previous '*' exists: backtrack to match 1 more char
            elif star_idx != -1:
                p_idx = star_idx + 1
                match_idx += 1
                s_idx = match_idx
            # 4. Mismatch with no preceding '*' to fall back on
            else:
                return False
        
        # Consume any trailing '*' characters in the pattern
        while p_idx < len(p) and p[p_idx] == '*':
            p_idx += 1
            
        return p_idx == len(p)