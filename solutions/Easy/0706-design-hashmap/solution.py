# ──────────────────────────────────────────────────
# Problem  : 706. Design HashMap
# Difficulty: Easy
# Tags     : Array, Hash Table, Linked List, Design, Hash Function
# Link     : https://leetcode.com/problems/design-hashmap/
# Runtime  : 0 ms (beats 0%)
# Memory   : 19532000 (beats 0%)
# Language : python3
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class ListNode:
    def __init__(self, key: int = -1, val: int = -1, next: 'ListNode' = None):
        self.key = key
        self.val = val
        self.next = next

class MyHashMap:

    def __init__(self):
        self.size = 1000
        # Initialize each bucket with a dummy head node
        self.buckets = [ListNode() for _ in range(self.size)]

    def _hash(self, key: int) -> int:
        return key % self.size

    def put(self, key: int, value: int) -> None:
        idx = self._hash(key)
        curr = self.buckets[idx]
        
        while curr.next:
            if curr.next.key == key:
                curr.next.val = value
                return
            curr = curr.next
            
        curr.next = ListNode(key, value)

    def get(self, key: int) -> int:
        idx = self._hash(key)
        curr = self.buckets[idx].next
        
        while curr:
            if curr.key == key:
                return curr.val
            curr = curr.next
            
        return -1

    def remove(self, key: int) -> None:
        idx = self._hash(key)
        curr = self.buckets[idx]
        
        while curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next
                return
            curr = curr.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key, value)
# param_2 = obj.get(key)
# obj.remove(key)