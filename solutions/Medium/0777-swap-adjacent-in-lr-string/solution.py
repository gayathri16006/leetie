# ──────────────────────────────────────────────────
# Problem  : 777. Swap Adjacent in LR String
# Difficulty: Medium
# Tags     : Two Pointers, String
# Link     : https://leetcode.com/problems/swap-adjacent-in-lr-string/
# Runtime  : 0 ms (beats 0%)
# Memory   : 19416000 (beats 0%)
# Language : python3
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        # Both strings must have identical relative order of non-'X' characters
        if start.replace("X", "") != end.replace("X", ""):
            return False
        
        n = len(start)
        i = j = 0
        
        while i < n and j < n:
            # Advance to the next non-'X' character in both strings
            while i < n and start[i] == "X":
                i += 1
            while j < n and end[j] == "X":
                j += 1
                
            if i < n and j < n:
                # 'L' can only move left (start index >= end index)
                if start[i] == "L" and i < j:
                    return False
                # 'R' can only move right (start index <= end index)
                if start[i] == "R" and i > j:
                    return False
                
                i += 1
                j += 1
                
        return True