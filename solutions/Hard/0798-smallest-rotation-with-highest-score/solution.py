# ──────────────────────────────────────────────────
# Problem  : 798. Smallest Rotation with Highest Score
# Difficulty: Hard
# Tags     : Array, Prefix Sum
# Link     : https://leetcode.com/problems/smallest-rotation-with-highest-score/
# Runtime  : 0 ms (beats 0%)
# Memory   : 19316000 (beats 0%)
# Language : python3
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def bestRotation(self, nums: list[int]) -> int:
        n = len(nums)
        # diff array to track changes in score for each rotation k
        diff = [0] * n
        
        # For each element nums[i], it scores a point if its new index >= nums[i].
        # When rotating by k, new_index = (i - k + n) % n.
        # Condition: (i - k + n) % n >= nums[i].
        # It loses a point when k goes from (i - nums[i] + n) % n to the next step.
        for i, val in enumerate(nums):
            # Interval of k where nums[i] contributes 1 point:
            # [(i + 1) % n, (i - val + n + 1) % n]
            left = (i + 1) % n
            right = (i - val + n + 1) % n
            
            diff[left] += 1
            diff[right] -= 1
            if left >= right:
                diff[0] += 1
                
        # Find the rotation k with the maximum cumulative score
        max_score = -1
        best_k = 0
        cur_score = 0
        
        for k in range(n):
            cur_score += diff[k]
            if cur_score > max_score:
                max_score = cur_score
                best_k = k
                
        return best_k