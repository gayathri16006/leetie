# ──────────────────────────────────────────────────
# Problem  : 3876. Construct Uniform Parity Array II
# Difficulty: Medium
# Tags     : Array, Math
# Link     : https://leetcode.com/problems/construct-uniform-parity-array-ii/
# Runtime  : 14 ms (beats 100%)
# Memory   : 21732000 (beats 62%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def uniformArray(self, nums1):
        """
        :type nums1: List[int]
        :rtype: bool
        """
        min_val = min(nums1)
        
        # If the minimum is odd, all evens can be converted to odd
        if min_val % 2 == 1:
            return True
            
        # If the minimum is even, it is only possible if there are no odd numbers
        return all(x % 2 == 0 for x in nums1)