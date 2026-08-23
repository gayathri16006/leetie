# ──────────────────────────────────────────────────
# Problem  : 599. Minimum Index Sum of Two Lists
# Difficulty: Easy
# Tags     : Array, Hash Table, String
# Link     : https://leetcode.com/problems/minimum-index-sum-of-two-lists/
# Runtime  : 11 ms (beats 56%)
# Memory   : 12596000 (beats 74%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        idx_map = {word: i for i, word in enumerate(list1)}
        min_sum = float('inf')
        res = []
        
        for j, word in enumerate(list2):
            if word in idx_map:
                current_sum = idx_map[word] + j
                if current_sum < min_sum:
                    min_sum = current_sum
                    res = [word]
                elif current_sum == min_sum:
                    res.append(word)
                    
        return res