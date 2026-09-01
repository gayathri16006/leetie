# ──────────────────────────────────────────────────
# Problem  : 786. K-th Smallest Prime Fraction
# Difficulty: Medium
# Tags     : Array, Two Pointers, Binary Search, Sorting, Heap (Priority Queue)
# Link     : https://leetcode.com/problems/k-th-smallest-prime-fraction/
# Runtime  : 19 ms (beats 95%)
# Memory   : 19328000 (beats 94%)
# Language : python3
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        left, right = 0.0, 1.0
        
        while left < right:
            mid = (left + right) / 2
            max_fraction = 0.0
            total_smaller = 0
            best_i, best_j = 0, 0
            j = 1
            
            for i in range(n - 1):
                while j < n and arr[i] > mid * arr[j]:
                    j += 1
                
                total_smaller += n - j
                
                if j == n:
                    break
                
                fraction = arr[i] / arr[j]
                if fraction > max_fraction:
                    max_fraction = fraction
                    best_i, best_j = i, j
            
            if total_smaller == k:
                return [arr[best_i], arr[best_j]]
            elif total_smaller < k:
                left = mid
            else:
                right = mid
                
        return []