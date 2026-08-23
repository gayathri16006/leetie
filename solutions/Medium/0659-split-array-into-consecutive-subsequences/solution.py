# ──────────────────────────────────────────────────
# Problem  : 659. Split Array into Consecutive Subsequences
# Difficulty: Medium
# Tags     : Array, Hash Table, Greedy, Heap (Priority Queue)
# Link     : https://leetcode.com/problems/split-array-into-consecutive-subsequences/
# Runtime  : 101 ms (beats 12%)
# Memory   : 13360000 (beats 51%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

from collections import Counter

class Solution(object):
    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        count = Counter(nums)
        end = Counter()  # end[x] tracks count of valid subsequences ending at x

        for x in nums:
            if count[x] == 0:
                continue

            count[x] -= 1

            # Option 1: Append to an existing subsequence ending at x - 1
            if end[x - 1] > 0:
                end[x - 1] -= 1
                end[x] += 1
            # Option 2: Form a new 3-element subsequence [x, x + 1, x + 2]
            elif count[x + 1] > 0 and count[x + 2] > 0:
                count[x + 1] -= 1
                count[x + 2] -= 1
                end[x + 2] += 1
            else:
                return False

        return True