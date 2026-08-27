# ──────────────────────────────────────────────────
# Problem  : 779. K-th Symbol in Grammar
# Difficulty: Medium
# Tags     : Math, Bit Manipulation, Recursion
# Link     : https://leetcode.com/problems/k-th-symbol-in-grammar/
# Runtime  : 0 ms (beats 0%)
# Memory   : 19360000 (beats 0%)
# Language : python3
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        # The value at index k (1-indexed) corresponds to the parity of set bits in (k - 1)
        return (k - 1).bit_count() % 2