# ──────────────────────────────────────────────────
# Problem  : 915. Partition Array into Disjoint Intervals
# Difficulty: Medium
# Tags     : Array
# Link     : https://leetcode.com/problems/partition-array-into-disjoint-intervals/
# Runtime  : 0 ms (beats 0%)
# Memory   : 12416000 (beats 0%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def partitionDisjoint(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left_max = nums[0]
        curr_max = nums[0]
        partition_idx = 0

        for i in range(1, len(nums)):
            curr_max = max(curr_max, nums[i])
            
            # An element smaller than left_max must belong to the left partition
            if nums[i] < left_max:
                left_max = curr_max
                partition_idx = i

        return partition_idx + 1