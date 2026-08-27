# ──────────────────────────────────────────────────
# Problem  : 752. Open the Lock
# Difficulty: Medium
# Tags     : Array, Hash Table, String, Breadth-First Search, Bidirectional Search
# Link     : https://leetcode.com/problems/open-the-lock/
# Runtime  : 339 ms (beats 64%)
# Memory   : 20476000 (beats 52%)
# Language : python3
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

from collections import deque

class Solution:
    def openLock(self, deadends: list[str], target: str) -> int:
        dead_set = set(deadends)
        start = "0000"
        
        if start in dead_set:
            return -1
        if start == target:
            return 0
        
        queue = deque([(start, 0)])
        visited = set([start])
        
        while queue:
            current, turns = queue.popleft()
            
            if current == target:
                return turns
            
            for i in range(4):
                digit = int(current[i])
                
                # Turn wheel clockwise and counter-clockwise
                for delta in (-1, 1):
                    new_digit = (digit + delta) % 10
                    next_state = current[:i] + str(new_digit) + current[i+1:]
                    
                    if next_state not in dead_set and next_state not in visited:
                        visited.add(next_state)
                        queue.append((next_state, turns + 1))
                        
        return -1