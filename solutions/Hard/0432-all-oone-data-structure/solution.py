# ──────────────────────────────────────────────────
# Problem  : 432. All O`one Data Structure
# Difficulty: Hard
# Tags     : Hash Table, Linked List, Design, Doubly-Linked List
# Link     : https://leetcode.com/problems/all-oone-data-structure/
# Runtime  : 0 ms (beats 0%)
# Memory   : 12428000 (beats 0%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Node:
    def __init__(self, count=0):
        self.count = count
        self.keys = set()
        self.prev = None
        self.next = None

class AllOne(object):

    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.map = {}  # key -> Node

    def _insert_after(self, prev_node, new_node):
        new_node.prev = prev_node
        new_node.next = prev_node.next
        prev_node.next.prev = new_node
        prev_node.next = new_node

    def _remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def inc(self, key):
        """
        :type key: str
        :rtype: None
        """
        if key in self.map:
            cur_node = self.map[key]
            next_node = cur_node.next
            cur_node.keys.remove(key)

            # Insert new bucket if one with count + 1 doesn't exist
            if next_node == self.tail or next_node.count != cur_node.count + 1:
                new_node = Node(cur_node.count + 1)
                self._insert_after(cur_node, new_node)
                next_node = new_node

            next_node.keys.add(key)
            self.map[key] = next_node

            if not cur_node.keys:
                self._remove_node(cur_node)
        else:
            first_node = self.head.next
            # Insert bucket for count 1 if it doesn't exist
            if first_node == self.tail or first_node.count != 1:
                new_node = Node(1)
                self._insert_after(self.head, new_node)
                first_node = new_node

            first_node.keys.add(key)
            self.map[key] = first_node

    def dec(self, key):
        """
        :type key: str
        :rtype: None
        """
        if key not in self.map:
            return

        cur_node = self.map[key]
        cur_node.keys.remove(key)

        if cur_node.count == 1:
            del self.map[key]
        else:
            prev_node = cur_node.prev
            # Insert bucket for count - 1 if it doesn't exist
            if prev_node == self.head or prev_node.count != cur_node.count - 1:
                new_node = Node(cur_node.count - 1)
                self._insert_after(prev_node, new_node)
                prev_node = new_node

            prev_node.keys.add(key)
            self.map[key] = prev_node

        if not cur_node.keys:
            self._remove_node(cur_node)

    def getMaxKey(self):
        """
        :rtype: str
        """
        if self.tail.prev == self.head:
            return ""
        return next(iter(self.tail.prev.keys))

    def getMinKey(self):
        """
        :rtype: str
        """
        if self.head.next == self.tail:
            return ""
        return next(iter(self.head.next.keys))