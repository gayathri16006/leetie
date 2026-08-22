# ──────────────────────────────────────────────────
# Problem  : 493. Reverse Pairs
# Difficulty: Hard
# Tags     : Array, Binary Search, Divide and Conquer, Binary Indexed Tree, Segment Tree, Merge Sort, Ordered Set, Treap
# Link     : https://leetcode.com/problems/reverse-pairs/
# Runtime  : 0 ms (beats 0%)
# Memory   : 12480000 (beats 0%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def merge_sort(start, end):
            if start >= end:
                return 0
            
            mid = (start + end) // 2
            count = merge_sort(start, mid) + merge_sort(mid + 1, end)
            
            # Count reverse pairs across the two sorted halves
            j = mid + 1
            for i in range(start, mid + 1):
                while j <= end and nums[i] > 2 * nums[j]:
                    j += 1
                count += (j - (mid + 1))
            
            # Standard merge step
            nums[start:end + 1] = sorted(nums[start:end + 1])
            return count

        return merge_sort(0, len(nums) - 1)