# ──────────────────────────────────────────────────
# Problem  : 551. Student Attendance Record I
# Difficulty: Easy
# Tags     : String
# Link     : https://leetcode.com/problems/student-attendance-record-i/
# Runtime  : 0 ms (beats 100%)
# Memory   : 12432000 (beats 18%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def checkRecord(self, s):
        return s.count('A') < 2 and 'LLL' not in s