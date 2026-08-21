# ──────────────────────────────────────────────────
# Problem  : 319. Bulb Switcher
# Difficulty: Medium
# Tags     : Math, Brainteaser
# Link     : https://leetcode.com/problems/bulb-switcher/
# Runtime  : 0 ms (beats 100%)
# Memory   : 12320000 (beats 56%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):

    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        return int(n**0.5)