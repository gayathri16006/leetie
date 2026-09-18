# ──────────────────────────────────────────────────
# Problem  : 944. Delete Columns to Make Sorted
# Difficulty: Easy
# Tags     : Array, String, Longest Increasing Subsequence
# Link     : https://leetcode.com/problems/delete-columns-to-make-sorted/
# Runtime  : 0 ms (beats 0%)
# Memory   : 12396000 (beats 0%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def minDeletionSize(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        ans = 0
        num_rows = len(strs)
        num_cols = len(strs[0])
        
        for col in range(num_cols):
            for row in range(num_rows - 1):
                if strs[row][col] > strs[row + 1][col]:
                    ans += 1
                    break
                    
        return ans