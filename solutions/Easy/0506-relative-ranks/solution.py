# ──────────────────────────────────────────────────
# Problem  : 506. Relative Ranks
# Difficulty: Easy
# Tags     : Array, Sorting, Heap (Priority Queue)
# Link     : https://leetcode.com/problems/relative-ranks/
# Runtime  : 8 ms (beats 48%)
# Memory   : 13264000 (beats 44%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        n = len(score)
        result = [""] * n
        
        # Sort (original_index, score_value) in descending order of score
        sorted_scores = sorted(enumerate(score), key=lambda x: x[1], reverse=True)
        
        medals = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        
        for rank, (original_idx, _) in enumerate(sorted_scores):
            if rank < 3:
                result[original_idx] = medals[rank]
            else:
                result[original_idx] = str(rank + 1)
                
        return result