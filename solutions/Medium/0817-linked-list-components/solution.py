# ──────────────────────────────────────────────────
# Problem  : 817. Linked List Components
# Difficulty: Medium
# Tags     : Array, Hash Table, Linked List
# Link     : https://leetcode.com/problems/linked-list-components/
# Runtime  : 0 ms (beats 0%)
# Memory   : 12336000 (beats 0%)
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
    def numComponents(self, head, nums):
        """
        :type head: Optional[ListNode]
        :type nums: List[int]
        :rtype: int
        """
        num_set = set(nums)
        count = 0
        curr = head
        
        while curr:
            # Check if the current node is the start/part of a component and the component ends here
            if curr.val in num_set and (curr.next is None or curr.next.val not in num_set):
                count += 1
            curr = curr.next
            
        return count