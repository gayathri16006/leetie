# ──────────────────────────────────────────────────
# Problem  : 763. Partition Labels
# Difficulty: Medium
# Tags     : Hash Table, Two Pointers, String, Greedy
# Link     : https://leetcode.com/problems/partition-labels/
# Runtime  : 4 ms (beats 40%)
# Memory   : 19296000 (beats 62%)
# Language : python3
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        # Record the last occurrence index of each character
        last_index = {char: i for i, char in enumerate(s)}
        
        partitions = []
        start = 0
        end = 0
        
        for i, char in enumerate(s):
            # Extend the current partition's boundary to the farthest last occurrence
            end = max(end, last_index[char])
            
            # When current index reaches the furthest required boundary, split here
            if i == end:
                partitions.append(end - start + 1)
                start = i + 1
                
        return partitions