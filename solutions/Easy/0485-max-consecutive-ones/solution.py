# ──────────────────────────────────────────────────
# Problem  : 485. Max Consecutive Ones
# Difficulty: Easy
# Tags     : Array
# Link     : https://leetcode.com/problems/max-consecutive-ones/
# Runtime  : 0 ms (beats 0%)
# Memory   : 12224000 (beats 0%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_count = 0
        current_count = 0

        for num in nums:
            if num == 1:
                current_count += 1
                max_count = max(max_count, current_count)
            else:
                current_count = 0

        return max_count