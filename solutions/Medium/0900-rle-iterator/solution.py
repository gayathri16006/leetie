# ──────────────────────────────────────────────────
# Problem  : 900. RLE Iterator
# Difficulty: Medium
# Tags     : Array, Design, Counting, Iterator
# Link     : https://leetcode.com/problems/rle-iterator/
# Runtime  : 0 ms (beats 100%)
# Memory   : 12828000 (beats 29%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class RLEIterator(object):

    def __init__(self, encoding):
        """
        :type encoding: List[int]
        """
        self.encoding = encoding
        self.index = 0

    def next(self, n):
        """
        :type n: int
        :rtype: int
        """
        while self.index < len(self.encoding):
            if n <= self.encoding[self.index]:
                self.encoding[self.index] -= n
                return self.encoding[self.index + 1]
            else:
                n -= self.encoding[self.index]
                self.index += 2
        return -1