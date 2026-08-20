# ──────────────────────────────────────────────────
# Problem  : 315. Count of Smaller Numbers After Self
# Difficulty: Hard
# Tags     : Array, Binary Search, Divide and Conquer, Binary Indexed Tree, Segment Tree, Merge Sort, Ordered Set, Treap
# Link     : https://leetcode.com/problems/count-of-smaller-numbers-after-self/
# Runtime  : 1916 ms (beats 43%)
# Memory   : 41472000 (beats 56%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        counts = [0] * n
        # Pair each number with its original index: (val, original_index)
        arr = [(val, i) for i, val in enumerate(nums)]
        
        def merge_sort(enum_arr):
            if len(enum_arr) <= 1:
                return enum_arr
            
            mid = len(enum_arr) // 2
            left = merge_sort(enum_arr[:mid])
            right = merge_sort(enum_arr[mid:])
            
            merged = []
            i = j = 0
            right_counter = 0  # Count of elements from right half smaller than left[i]
            
            while i < len(left) and j < len(right):
                if right[j][0] < left[i][0]:
                    merged.append(right[j])
                    right_counter += 1
                    j += 1
                else:
                    merged.append(left[i])
                    counts[left[i][1]] += right_counter
                    i += 1
            
            while i < len(left):
                merged.append(left[i])
                counts[left[i][1]] += right_counter
                i += 1
                
            while j < len(right):
                merged.append(right[j])
                j += 1
                
            return merged

        merge_sort(arr)
        return counts