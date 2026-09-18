# ──────────────────────────────────────────────────
# Problem  : 923. 3Sum With Multiplicity
# Difficulty: Medium
# Tags     : Array, Hash Table, Two Pointers, Sorting, Counting
# Link     : https://leetcode.com/problems/3sum-with-multiplicity/
# Runtime  : 10 ms (beats 89%)
# Memory   : 12568000 (beats 32%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

from collections import Counter

class Solution(object):
    def threeSumMulti(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """
        MOD = 10**9 + 7
        count = Counter(arr)
        keys = sorted(count.keys())
        ans = 0
        n = len(keys)

        for i in range(n):
            x = keys[i]
            # Case 1: x == y == z
            if 3 * x == target:
                ans += count[x] * (count[x] - 1) * (count[x] - 2) // 6

            for j in range(i, n):
                y = keys[j]
                z = target - x - y

                if z < y:
                    continue
                if z not in count:
                    continue

                if x == y and y < z:
                    # Case 2: x == y < z
                    ans += (count[x] * (count[x] - 1) // 2) * count[z]
                elif x < y and y == z:
                    # Case 3: x < y == z
                    ans += count[x] * (count[y] * (count[y] - 1) // 2)
                elif x < y and y < z:
                    # Case 4: x < y < z
                    ans += count[x] * count[y] * count[z]

        return ans % MOD