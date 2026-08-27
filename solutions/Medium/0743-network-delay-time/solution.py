# ──────────────────────────────────────────────────
# Problem  : 743. Network Delay Time
# Difficulty: Medium
# Tags     : Depth-First Search, Breadth-First Search, Graph Theory, Heap (Priority Queue), Shortest Path, Dijkstra's Algorithm
# Link     : https://leetcode.com/problems/network-delay-time/
# Runtime  : 357 ms (beats 19%)
# Memory   : 22080000 (beats 9%)
# Language : python3
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

from collections import defaultdict
import heapq

class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        # Build adjacency list: u -> [(v, w)]
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
            
        # Priority queue for Dijkstra's: (accumulated_time, current_node)
        pq = [(0, k)]
        distances = {}
        
        while pq:
            time, node = heapq.heappop(pq)
            
            if node in distances:
                continue
            distances[node] = time
            
            for neighbor, weight in graph[node]:
                if neighbor not in distances:
                    heapq.heappush(pq, (time + weight, neighbor))
                    
        # If all n nodes are reached, return max time; otherwise return -1
        return max(distances.values()) if len(distances) == n else -1