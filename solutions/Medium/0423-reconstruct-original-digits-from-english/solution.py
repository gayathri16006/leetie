# ──────────────────────────────────────────────────
# Problem  : 423. Reconstruct Original Digits from English
# Difficulty: Medium
# Tags     : Hash Table, Math, String
# Link     : https://leetcode.com/problems/reconstruct-original-digits-from-english/
# Runtime  : 54 ms (beats 40%)
# Memory   : 12524000 (beats 58%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

from collections import Counter

class Solution(object):
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        count = Counter(s)
        digits = [0] * 10
        
        # Primary unique characters
        digits[0] = count['z']
        digits[2] = count['w']
        digits[4] = count['u']
        digits[6] = count['x']
        digits[8] = count['g']
        
        # Secondary derived counts
        digits[3] = count['h'] - digits[8]
        digits[5] = count['f'] - digits[4]
        digits[7] = count['s'] - digits[6]
        digits[1] = count['o'] - digits[0] - digits[2] - digits[4]
        digits[9] = count['i'] - digits[5] - digits[6] - digits[8]
        
        # Build output string in ascending order
        return "".join(str(i) * digits[i] for i in range(10))