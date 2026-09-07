# ──────────────────────────────────────────────────
# Problem  : 922. Sort Array By Parity II
# Difficulty: Easy
# Tags     : Array, Two Pointers, Sorting
# Link     : https://leetcode.com/problems/sort-array-by-parity-ii/
# Runtime  : 0 ms (beats 0%)
# Memory   : 12260000 (beats 0%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def sortArrayByParityII(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        j = 1  # Tracks odd indices

        for i in range(0, n, 2):
            # If an even index contains an odd number
            if nums[i] % 2 != 0:
                # Find the next odd index that contains an even number
                while nums[j] % 2 != 0:
                    j += 2
                # Swap them into their correct positions
                nums[i], nums[j] = nums[j], nums[i]

        return nums