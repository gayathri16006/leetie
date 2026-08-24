# ──────────────────────────────────────────────────
# Problem  : 629. K Inverse Pairs Array
# Difficulty: Hard
# Tags     : Dynamic Programming
# Link     : https://leetcode.com/problems/k-inverse-pairs-array/
# Runtime  : 252 ms (beats 25%)
# Memory   : 12540000 (beats 36%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def kInversePairs(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        MOD = 10**9 + 7
        
        # Max inverse pairs possible with n numbers is n * (n - 1) // 2
        if k < 0 or k > n * (n - 1) // 2:
            return 0
        if k == 0:
            return 1
            
        # dp[j] stores the number of arrays of current size with j inverse pairs
        dp = [0] * (k + 1)
        dp[0] = 1
        
        for i in range(1, n + 1):
            next_dp = [0] * (k + 1)
            window_sum = 0
            
            for j in range(k + 1):
                window_sum = (window_sum + dp[j]) % MOD
                
                # Maintain sliding window of size i
                if j >= i:
                    window_sum = (window_sum - dp[j - i] + MOD) % MOD
                
                next_dp[j] = window_sum
                
            dp = next_dp
            
        return dp[k]