# ──────────────────────────────────────────────────
# Problem  : 415. Add Strings
# Difficulty: Easy
# Tags     : Math, String, Simulation
# Link     : https://leetcode.com/problems/add-strings/
# Runtime  : 7 ms (beats 48%)
# Memory   : 12408000 (beats 57%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        p1 = len(num1) - 1
        p2 = len(num2) - 1
        carry = 0
        res = []

        while p1 >= 0 or p2 >= 0 or carry:
            # Convert character digits to integer using ASCII values (ord)
            d1 = ord(num1[p1]) - ord('0') if p1 >= 0 else 0
            d2 = ord(num2[p2]) - ord('0') if p2 >= 0 else 0

            total = d1 + d2 + carry
            carry = total // 10
            res.append(str(total % 10))

            p1 -= 1
            p2 -= 1

        # The digits were appended from least to most significant, so reverse the result
        return "".join(reversed(res))