# ──────────────────────────────────────────────────
# Problem  : 839. Similar String Groups
# Difficulty: Hard
# Tags     : Array, Hash Table, String, Depth-First Search, Breadth-First Search, Union-Find
# Link     : https://leetcode.com/problems/similar-string-groups/
# Runtime  : 812 ms (beats 53%)
# Memory   : 12720000 (beats 18%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def numSimilarGroups(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        # Deduplicate identical strings to optimize checks
        strs = list(set(strs))
        n = len(strs)
        
        parent = list(range(n))
        
        def find(i):
            if parent[i] == i:
                return i
            parent[i] = find(parent[i])
            return parent[i]
        
        def union(i, j):
            root_i = find(i)
            root_j = find(j)
            if root_i != root_j:
                parent[root_i] = root_j
                return True
            return False

        def is_similar(s1, s2):
            diff = 0
            for c1, c2 in zip(s1, s2):
                if c1 != c2:
                    diff += 1
                    if diff > 2:
                        return False
            return diff == 0 or diff == 2

        groups = n
        for i in range(n):
            for j in range(i + 1, n):
                if is_similar(strs[i], strs[j]):
                    if union(i, j):
                        groups -= 1

        return groups