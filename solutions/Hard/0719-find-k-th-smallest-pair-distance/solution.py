# ──────────────────────────────────────────────────
# Problem  : 719. Find K-th Smallest Pair Distance
# Difficulty: Hard
# Tags     : Array, Two Pointers, Binary Search, Sorting
# Link     : https://leetcode.com/problems/find-k-th-smallest-pair-distance/
# Runtime  : 32 ms (beats 46%)
# Memory   : 19948000 (beats 34%)
# Language : python3
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def smallestDistancePair(self, nums: list[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        
        # Helper function to count pairs with distance <= mid
        def countPairs(mid: int) -> int:
            count = 0
            left = 0
            for right in range(n):
                while nums[right] - nums[left] > mid:
                    left += 1
                count += right - left
            return count

        # Binary search over the range of possible distances
        low = 0
        high = nums[-1] - nums[0]
        
        while low < high:
            mid = (low + high) // 2
            if countPairs(mid) >= k:
                high = mid
            else:
                low = mid + 1
                
        return low