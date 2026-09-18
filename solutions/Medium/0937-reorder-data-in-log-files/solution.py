# ──────────────────────────────────────────────────
# Problem  : 937. Reorder Data in Log Files
# Difficulty: Medium
# Tags     : Array, String, Sorting
# Link     : https://leetcode.com/problems/reorder-data-in-log-files/
# Runtime  : 0 ms (beats 0%)
# Memory   : 12456000 (beats 0%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        def get_key(log):
            identifier, rest = log.split(" ", 1)
            # Letter-logs: indicator 0, then content, then identifier
            # Digit-logs: indicator 1 (preserves relative order due to Python's stable sort)
            if rest[0].isalpha():
                return (0, rest, identifier)
            return (1,)

        return sorted(logs, key=get_key)