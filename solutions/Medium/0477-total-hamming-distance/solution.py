# ──────────────────────────────────────────────────
# Problem  : 477. Total Hamming Distance
# Difficulty: Medium
# Tags     : Array, Math, Bit Manipulation
# Link     : https://leetcode.com/problems/total-hamming-distance/
# Runtime  : 156 ms (beats 64%)
# Memory   : 13220000 (beats 86%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):

    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total_distance = 0
        n = len(nums)

        # Numbers are bounded by 10^9 < 2^30, so check 30 bit positions (0 to 29)
        for bit in range(30):
            count_ones = 0
            for num in nums:
                if (num >> bit) & 1:
                    count_ones += 1

            count_zeros = n - count_ones
            # Number of pairs with differing bits at this position
            total_distance += count_ones * count_zeros

        return total_distance
        