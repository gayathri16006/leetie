# ──────────────────────────────────────────────────
# Problem  : 933. Number of Recent Calls
# Difficulty: Easy
# Tags     : Design, Queue, Data Stream
# Link     : https://leetcode.com/problems/number-of-recent-calls/
# Runtime  : 60 ms (beats 70%)
# Memory   : 17160000 (beats 91%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

from collections import deque

class RecentCounter(object):

    def __init__(self):
        self.requests = deque()

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.requests.append(t)
        while self.requests and self.requests[0] < t - 3000:
            self.requests.popleft()
        return len(self.requests)


