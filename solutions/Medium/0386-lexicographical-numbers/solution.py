# ──────────────────────────────────────────────────
# Problem  : 386. Lexicographical Numbers
# Difficulty: Medium
# Tags     : Depth-First Search, Trie
# Link     : https://leetcode.com/problems/lexicographical-numbers/
# Runtime  : 13 ms (beats 74%)
# Memory   : 19320000 (beats 62%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):

    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = []
        curr = 1

        for _ in range(n):
            res.append(curr)

            # 1. Try to go deeper (e.g., 1 -> 10 -> 100)
            if curr * 10 <= n:
                curr *= 10
            else:
                # 2. If we reach the bound or end with 9, backtrack to the parent branch
                while curr % 10 == 9 or curr + 1 > n:
                    curr //= 10

                # Move to the next sibling
                curr += 1

        return res