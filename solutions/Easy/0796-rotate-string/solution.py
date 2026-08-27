# ──────────────────────────────────────────────────
# Problem  : 796. Rotate String
# Difficulty: Easy
# Tags     : String, String Matching
# Link     : https://leetcode.com/problems/rotate-string/
# Runtime  : 0 ms (beats 100%)
# Memory   : 19188000 (beats 87%)
# Language : python3
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # A rotation of s is valid if goal has the same length and is a substring of s + s
        return len(s) == len(goal) and goal in (s + s)