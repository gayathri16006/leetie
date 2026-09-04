# ──────────────────────────────────────────────────
# Problem  : 904. Fruit Into Baskets
# Difficulty: Medium
# Tags     : Array, Hash Table, Sliding Window
# Link     : https://leetcode.com/problems/fruit-into-baskets/
# Runtime  : 264 ms (beats 52%)
# Memory   : 17012000 (beats 60%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

from collections import defaultdict

class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        count = defaultdict(int)
        left = 0
        max_fruits = 0

        for right in range(len(fruits)):
            count[fruits[right]] += 1

            # Shrink window if more than 2 distinct fruit types exist
            while len(count) > 2:
                count[fruits[left]] -= 1
                if count[fruits[left]] == 0:
                    del count[fruits[left]]
                left += 1

            max_fruits = max(max_fruits, right - left + 1)

        return max_fruits