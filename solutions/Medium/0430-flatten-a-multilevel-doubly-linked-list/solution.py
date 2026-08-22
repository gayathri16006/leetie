# ──────────────────────────────────────────────────
# Problem  : 430. Flatten a Multilevel Doubly Linked List
# Difficulty: Medium
# Tags     : Linked List, Depth-First Search, Doubly-Linked List
# Link     : https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/
# Runtime  : 30 ms (beats 25%)
# Memory   : 12852000 (beats 47%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution(object):
    def flatten(self, head):
        if not head:
            return None
        
        curr = head
        stack = []
        
        while curr:
            # If current node has a child branch
            if curr.child:
                # If there is a next node, save it to reconnect later
                if curr.next:
                    stack.append(curr.next)
                
                # Connect curr to child
                curr.next = curr.child
                curr.child.prev = curr
                curr.child = None  # Remove the child pointer
            
            # If at the end of the current level and there are nodes saved in stack
            if not curr.next and stack:
                next_node = stack.pop()
                curr.next = next_node
                next_node.prev = curr
            
            curr = curr.next
            
        return head