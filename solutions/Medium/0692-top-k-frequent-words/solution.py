# ──────────────────────────────────────────────────
# Problem  : 692. Top K Frequent Words
# Difficulty: Medium
# Tags     : Array, Hash Table, String, Trie, Sorting, Heap (Priority Queue), Bucket Sort, Counting
# Link     : https://leetcode.com/problems/top-k-frequent-words/
# Runtime  : 1 ms (beats 69%)
# Memory   : 19564000 (beats 19%)
# Language : python3
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

from collections import Counter
import heapq
from typing import List

class Element:
    def __init__(self, word: str, freq: int):
        self.word = word
        self.freq = freq
        
    def __lt__(self, other: 'Element') -> bool:
        # Min-heap comparison:
        # 1. Lower frequency gets popped first.
        # 2. If frequencies match, lexicographically larger word gets popped first.
        if self.freq != other.freq:
            return self.freq < other.freq
        return self.word > other.word

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counts = Counter(words)
        heap = []
        
        for word, freq in counts.items():
            heapq.heappush(heap, Element(word, freq))
            if len(heap) > k:
                heapq.heappop(heap)
                
        # The heap contains the top k elements in reverse extraction order
        res = []
        while heap:
            res.append(heapq.heappop(heap).word)
            
        return res[::-1]