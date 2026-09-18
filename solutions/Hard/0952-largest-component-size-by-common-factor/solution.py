# ──────────────────────────────────────────────────
# Problem  : 952. Largest Component Size by Common Factor
# Difficulty: Hard
# Tags     : Array, Hash Table, Math, Union-Find, Number Theory, Prime Factorization
# Link     : https://leetcode.com/problems/largest-component-size-by-common-factor/
# Runtime  : 0 ms (beats 0%)
# Memory   : 12284000 (beats 0%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

from collections import Counter

class UnionFind(object):
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.parent[root_x] = root_y

class Solution(object):
    def largestComponentSize(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_val = max(nums)
        uf = UnionFind(max_val + 1)

        # Union each number with its prime factors
        for num in nums:
            d = 2
            val = num
            while d * d <= val:
                if val % d == 0:
                    uf.union(num, d)
                    while val % d == 0:
                        val //= d
                d += 1
            if val > 1:
                uf.union(num, val)

        # Find the size of the largest connected component of elements in nums
        counts = Counter(uf.find(num) for num in nums)
        return max(counts.values())