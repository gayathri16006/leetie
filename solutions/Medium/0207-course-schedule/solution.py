# ──────────────────────────────────────────────────
# Problem  : 207. Course Schedule
# Difficulty: Medium
# Tags     : Depth-First Search, Breadth-First Search, Graph Theory, Topological Sort, Directed Acyclic Graph
# Link     : https://leetcode.com/problems/course-schedule/
# Runtime  : 2 ms (beats 89%)
# Memory   : 20412000 (beats 62%)
# Language : python3
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

from collections import deque

class Solution:
    def canFinish(self, numCourses, prerequisites):
        g = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for a, b in prerequisites:
            g[b].append(a)
            indegree[a] += 1

        q = deque(i for i in range(numCourses) if indegree[i] == 0)
        count = 0

        while q:
            u = q.popleft()
            count += 1

            for v in g[u]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    q.append(v)

        return count == numCourses