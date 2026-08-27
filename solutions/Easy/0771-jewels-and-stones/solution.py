# ──────────────────────────────────────────────────
# Problem  : 771. Jewels and Stones
# Difficulty: Easy
# Tags     : Hash Table, String
# Link     : https://leetcode.com/problems/jewels-and-stones/
# Runtime  : 0 ms (beats 0%)
# Memory   : 19296000 (beats 0%)
# Language : python3
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewel_set = set(jewels)
        return sum(1 for stone in stones if stone in jewel_set)