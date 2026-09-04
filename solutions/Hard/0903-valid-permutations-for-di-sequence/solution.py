# ──────────────────────────────────────────────────
# Problem  : 903. Valid Permutations for DI Sequence
# Difficulty: Hard
# Tags     : String, Dynamic Programming, Prefix Sum
# Link     : https://leetcode.com/problems/valid-permutations-for-di-sequence/
# Runtime  : 0 ms (beats 0%)
# Memory   : 12524000 (beats 0%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def numPermsDISequence(self, s):
        """
        :type s: str
        :rtype: int
        """
        MOD = 10**9 + 7
        n = len(s)
        
        # dp[j] represents ways to form prefix with last element having relative rank j
        dp = [1]

        for i, ch in enumerate(s, 1):
            new_dp = [0] * (i + 1)
            
            if ch == 'I':
                # Prefix sum: dp[i][j] = sum(dp[i-1][k]) for k from 0 to j-1
                running_sum = 0
                for j in range(1, i + 1):
                    running_sum = (running_sum + dp[j - 1]) % MOD
                    new_dp[j] = running_sum
            else:
                # Suffix sum: dp[i][j] = sum(dp[i-1][k]) for k from j to i-1
                running_sum = 0
                for j in range(i - 1, -1, -1):
                    running_sum = (running_sum + dp[j]) % MOD
                    new_dp[j] = running_sum

            dp = new_dp

        return sum(dp) % MOD