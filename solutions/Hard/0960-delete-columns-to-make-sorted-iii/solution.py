# ──────────────────────────────────────────────────
# Problem  : 960. Delete Columns to Make Sorted III
# Difficulty: Hard
# Tags     : Array, String, Dynamic Programming
# Link     : https://leetcode.com/problems/delete-columns-to-make-sorted-iii/
# Runtime  : 151 ms (beats 82%)
# Memory   : 12508000 (beats 0%)
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
        m = len(strs[0])
        # dp[i] represents the length of the longest valid subsequence of columns ending at column i
        dp = [1] * m
        
        for i in range(m):
            for j in range(i):
                # Check if column j can precede column i across all rows
                if all(s[j] <= s[i] for s in strs):
                    dp[i] = max(dp[i], dp[j] + 1)
                    
        # Minimum deletions = total columns - maximum columns kept
        return m - max(dp)