# ──────────────────────────────────────────────────
# Problem  : 698. Partition to K Equal Sum Subsets
# Difficulty: Medium
# Tags     : Array, Dynamic Programming, Backtracking, Bit Manipulation, Memoization, Bitmask
# Link     : https://leetcode.com/problems/partition-to-k-equal-sum-subsets/
# Runtime  : 0 ms (beats 0%)
# Memory   : 19236000 (beats 0%)
# Language : python3
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

from typing import List

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        
        # Total sum must be divisible by k
        if total % k != 0:
            return False
        
        target = total // k
        nums.sort(reverse=True)
        
        # If the largest element exceeds target, partitioning is impossible
        if nums[0] > target:
            return False
        
        n = len(nums)
        memo = {}

        def backtrack(mask: int, curr_sum: int, remaining_k: int) -> bool:
            if remaining_k == 0:
                return True
            
            if mask in memo:
                return memo[mask]
            
            # If current subset reaches target, start building the next subset
            if curr_sum == target:
                res = backtrack(mask, 0, remaining_k - 1)
                memo[mask] = res
                return res
            
            for i in range(n):
                # Skip if element is already used
                if mask & (1 << i):
                    continue
                
                # Prune branches that exceed target
                if curr_sum + nums[i] > target:
                    continue
                
                # Try adding nums[i] to current subset
                if backtrack(mask | (1 << i), curr_sum + nums[i], remaining_k):
                    memo[mask] = True
                    return True
                
                # If placing nums[i] in an empty bucket fails, all symmetric choices also fail
                if curr_sum == 0:
                    break
                    
            memo[mask] = False
            return False

        return backtrack(0, 0, k)