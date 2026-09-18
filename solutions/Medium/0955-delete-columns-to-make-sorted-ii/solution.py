# ──────────────────────────────────────────────────
# Problem  : 955. Delete Columns to Make Sorted II
# Difficulty: Medium
# Tags     : Array, String, Greedy
# Link     : https://leetcode.com/problems/delete-columns-to-make-sorted-ii/
# Runtime  : 3 ms (beats 92%)
# Memory   : 12540000 (beats 6%)
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
        n = len(strs)
        word_len = len(strs[0])
        
        # sorted_pairs[i] is True if strs[i] < strs[i + 1] has been strictly determined
        is_sorted = [False] * (n - 1)
        deletions = 0
        
        for j in range(word_len):
            # Check if keeping column j violates the lexicographical order
            should_delete = False
            for i in range(n - 1):
                if not is_sorted[i] and strs[i][j] > strs[i + 1][j]:
                    should_delete = True
                    break
            
            if should_delete:
                deletions += 1
            else:
                # Column is kept; update which adjacent pairs are strictly sorted
                for i in range(n - 1):
                    if not is_sorted[i] and strs[i][j] < strs[i + 1][j]:
                        is_sorted[i] = True
                        
        return deletions