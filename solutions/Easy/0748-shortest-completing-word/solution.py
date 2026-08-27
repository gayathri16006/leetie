# ──────────────────────────────────────────────────
# Problem  : 748. Shortest Completing Word
# Difficulty: Easy
# Tags     : Array, Hash Table, String
# Link     : https://leetcode.com/problems/shortest-completing-word/
# Runtime  : 35 ms (beats 17%)
# Memory   : 19552000 (beats 43%)
# Language : python3
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

from collections import Counter

class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: list[str]) -> str:
        # Count target characters from licensePlate (lowercase letters only)
        target_counts = Counter(c.lower() for c in licensePlate if c.isalpha())
        
        result = None
        
        for word in words:
            word_counts = Counter(word)
            
            # Check if current word satisfies all character frequencies
            if all(word_counts[char] >= count for char, count in target_counts.items()):
                # Keep the shortest valid word; preserves first occurrence order on ties
                if result is None or len(word) < len(result):
                    result = word
                    
        return result