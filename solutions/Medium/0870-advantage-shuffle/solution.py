# ──────────────────────────────────────────────────
# Problem  : 870. Advantage Shuffle
# Difficulty: Medium
# Tags     : Array, Two Pointers, Greedy, Sorting
# Link     : https://leetcode.com/problems/advantage-shuffle/
# Runtime  : 126 ms (beats 88%)
# Memory   : 29720000 (beats 91%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def advantageCount(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1.sort()
        # Sort indices of nums2 based on value in descending order
        sorted_indices = sorted(range(len(nums2)), key=lambda i: nums2[i], reverse=True)
        
        ans = [0] * len(nums1)
        left = 0
        right = len(nums1) - 1
        
        for idx in sorted_indices:
            # If nums1's largest element beats nums2[idx], use it
            if nums1[right] > nums2[idx]:
                ans[idx] = nums1[right]
                right -= 1
            else:
                # Otherwise, waste nums1's smallest element
                ans[idx] = nums1[left]
                left += 1
                
        return ans