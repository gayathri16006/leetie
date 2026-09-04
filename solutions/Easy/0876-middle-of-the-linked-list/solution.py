# ──────────────────────────────────────────────────
# Problem  : 876. Middle of the Linked List
# Difficulty: Easy
# Tags     : Linked List, Two Pointers
# Link     : https://leetcode.com/problems/middle-of-the-linked-list/
# Runtime  : 0 ms (beats 100%)
# Memory   : 12316000 (beats 61%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow