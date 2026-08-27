# ──────────────────────────────────────────────────
# Problem  : 718. Maximum Length of Repeated Subarray
# Difficulty: Medium
# Tags     : Array, Binary Search, Dynamic Programming, Sliding Window, Rolling Hash, Hash Function
# Link     : https://leetcode.com/problems/maximum-length-of-repeated-subarray/
# Runtime  : 0 ms (beats 0%)
# Memory   : 19264000 (beats 0%)
# Language : python3
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def findLength(self, nums1: list[int], nums2: list[int]) -> int:
        n, m = len(nums1), len(nums2)
        # dp[j] stores the length of the longest common suffix ending at nums1[i-1] and nums2[j-1]
        dp = [0] * (m + 1)
        max_len = 0
        
        for i in range(1, n + 1):
            # Traverse backwards to use 1D array DP
            for j in range(m, 0, -1):
                if nums1[i - 1] == nums2[j - 1]:
                    dp[j] = dp[j - 1] + 1
                    max_len = max(max_len, dp[j])
                else:
                    dp[j] = 0
                    
        return max_len