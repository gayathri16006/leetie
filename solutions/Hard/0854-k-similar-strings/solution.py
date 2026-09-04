# ──────────────────────────────────────────────────
# Problem  : 854. K-Similar Strings
# Difficulty: Hard
# Tags     : Hash Table, String, Breadth-First Search
# Link     : https://leetcode.com/problems/k-similar-strings/
# Runtime  : 0 ms (beats 0%)
# Memory   : 12360000 (beats 0%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

from collections import deque

class Solution(object):
    def kSimilarity(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        if s1 == s2:
            return 0

        queue = deque([(s1, 0)])
        visited = {s1}

        while queue:
            curr, steps = queue.popleft()

            if curr == s2:
                return steps

            # Find the first index where curr differs from s2
            i = 0
            while i < len(curr) and curr[i] == s2[i]:
                i += 1

            # Find all valid positions j to swap with i
            curr_list = list(curr)
            for j in range(i + 1, len(curr)):
                if curr[j] == s2[i] and curr[j] != s2[j]:
                    # Perform swap
                    curr_list[i], curr_list[j] = curr_list[j], curr_list[i]
                    next_str = "".join(curr_list)

                    if next_str not in visited:
                        if next_str == s2:
                            return steps + 1
                        visited.add(next_str)
                        queue.append((next_str, steps + 1))

                    # Backtrack swap
                    curr_list[i], curr_list[j] = curr_list[j], curr_list[i]

                    # Greedy optimization: if swapping fixes both positions, prefer it immediately
                    if curr[i] == s2[j]:
                        break

        return -1