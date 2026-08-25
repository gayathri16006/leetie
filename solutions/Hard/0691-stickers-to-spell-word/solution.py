# ──────────────────────────────────────────────────
# Problem  : 691. Stickers to Spell Word
# Difficulty: Hard
# Tags     : Array, Hash Table, String, Dynamic Programming, Backtracking, Bit Manipulation, Memoization, Bitmask
# Link     : https://leetcode.com/problems/stickers-to-spell-word/
# Runtime  : 133 ms (beats 70%)
# Memory   : 20796000 (beats 44%)
# Language : python3
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

from collections import Counter
from typing import List

class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        # Precompute character frequencies for each sticker
        sticker_counts = [Counter(sticker) for sticker in stickers]
        
        # Memoization cache: remaining target string -> minimum stickers needed
        memo = {"": 0}
        
        def dfs(remaining: str) -> int:
            if remaining in memo:
                return memo[remaining]
            
            res = float('inf')
            first_char = remaining[0]
            
            # Prune search space: only use stickers that contain the first character of the remaining string
            for s_count in sticker_counts:
                if s_count[first_char] == 0:
                    continue
                
                # Consume matching characters from remaining string using current sticker
                temp_count = s_count.copy()
                next_rem = []
                for ch in remaining:
                    if temp_count[ch] > 0:
                        temp_count[ch] -= 1
                    else:
                        next_rem.append(ch)
                        
                sub_res = dfs("".join(next_rem))
                if sub_res != -1:
                    res = min(res, 1 + sub_res)
                    
            memo[remaining] = res if res != float('inf') else -1
            return memo[remaining]
            
        return dfs(target)