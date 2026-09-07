# ──────────────────────────────────────────────────
# Problem  : 930. Binary Subarrays With Sum
# Difficulty: Medium
# Tags     : Array, Hash Table, Sliding Window, Prefix Sum
# Link     : https://leetcode.com/problems/binary-subarrays-with-sum/
# Runtime  : 36 ms (beats 62%)
# Memory   : 17788000 (beats 6%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

from collections import defaultdict

class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        """
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """
        count = defaultdict(int)
        count[0] = 1  # Base case: a prefix sum of 0 has occurred once
        
        curr_sum = 0
        ans = 0
        
        for num in nums:
            curr_sum += num
            ans += count[curr_sum - goal]
            count[curr_sum] += 1
            
        return ans