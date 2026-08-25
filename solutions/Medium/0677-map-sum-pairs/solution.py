# ──────────────────────────────────────────────────
# Problem  : 677. Map Sum Pairs
# Difficulty: Medium
# Tags     : Hash Table, String, Design, Trie
# Link     : https://leetcode.com/problems/map-sum-pairs/
# Runtime  : 0 ms (beats 100%)
# Memory   : 19456000 (beats 47%)
# Language : python3
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class TrieNode:
    def __init__(self):
        self.children = {}
        self.val = 0

class MapSum:

    def __init__(self):
        self.root = TrieNode()
        # Track existing keys and their current values to compute delta updates
        self.map = {}

    def insert(self, key: str, val: int) -> None:
        delta = val - self.map.get(key, 0)
        self.map[key] = val
        
        curr = self.root
        curr.val += delta
        for ch in key:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
            curr.val += delta

    def sum(self, prefix: str) -> int:
        curr = self.root
        for ch in prefix:
            if ch not in curr.children:
                return 0
            curr = curr.children[ch]
            
        return curr.val


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key, val)
# param_2 = obj.sum(prefix)