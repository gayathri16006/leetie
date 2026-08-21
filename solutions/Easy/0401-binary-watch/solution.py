# ──────────────────────────────────────────────────
# Problem  : 401. Binary Watch
# Difficulty: Easy
# Tags     : Backtracking, Bit Manipulation
# Link     : https://leetcode.com/problems/binary-watch/
# Runtime  : 0 ms (beats 100%)
# Memory   : 12380000 (beats 52%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):

    def readBinaryWatch(self, turnedOn):
        """
        :type turnedOn: int
        :rtype: List[str]
        """
        res = []

        # Iterate through all valid hours and minutes
        for h in range(12):
            for m in range(60):
                # Count total set bits for the hour and minute combination
                if (bin(h).count("1") + bin(m).count("1")) == turnedOn:
                    # Minutes must be formatted with 2 digits (e.g. 05)
                    res.append("{:d}:{:02d}".format(h, m))

        return res