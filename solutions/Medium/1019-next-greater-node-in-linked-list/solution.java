// ──────────────────────────────────────────────────
// Problem  : 1019. Next Greater Node In Linked List
// Difficulty: Medium
// Tags     : Array, Linked List, Stack, Monotonic Stack
// Link     : https://leetcode.com/problems/next-greater-node-in-linked-list/
// Runtime  : 16 ms (beats 91%)
// Memory   : 49620000 (beats 59%)
// Language : java
// Copyright: (c) 2026 gayathri16006. All rights reserved.
// Synced by: leetie
// ──────────────────────────────────────────────────

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public int[] nextLargerNodes(ListNode head) {
        // Step 1: Convert linked list to an ArrayList for indexed access
        List<Integer> values = new ArrayList<>();
        while (head != null) {
            values.add(head.val);
            head = head.next;
        }

        int n = values.size();
        int[] answer = new int[n];
        // Stack stores indices of elements looking for their next greater element
        Deque<Integer> stack = new ArrayDeque<>();

        // Step 2: Iterate through elements and maintain a monotonic decreasing stack
        for (int i = 0; i < n; i++) {
            while (!stack.isEmpty() && values.get(stack.peek()) < values.get(i)) {
                answer[stack.pop()] = values.get(i);
            }
            stack.push(i);
        }

        return answer;
    }
}