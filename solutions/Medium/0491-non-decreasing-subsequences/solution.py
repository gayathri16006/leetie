# ──────────────────────────────────────────────────
# Problem  : 491. Non-decreasing Subsequences
# Difficulty: Medium
# Tags     : Array, Hash Table, Backtracking, Bit Manipulation
# Link     : https://leetcode.com/problems/non-decreasing-subsequences/
# Runtime  : 0 ms (beats 0%)
# Memory   : 12448000 (beats 0%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []

        def backtrack(start_index, path):
            if len(path) >= 2:
                result.append(list(path))

            used_in_level = set()

            for i in range(start_index, len(nums)):
                if nums[i] in used_in_level:
                    continue

                if not path or nums[i] >= path[-1]:
                    used_in_level.add(nums[i])
                    path.append(nums[i])
                    backtrack(i + 1, path)
                    path.pop()

        backtrack(0, [])
        return result