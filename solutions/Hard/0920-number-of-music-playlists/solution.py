# ──────────────────────────────────────────────────
# Problem  : 920. Number of Music Playlists
# Difficulty: Hard
# Tags     : Math, Dynamic Programming, Combinatorics
# Link     : https://leetcode.com/problems/number-of-music-playlists/
# Runtime  : 23 ms (beats 68%)
# Memory   : 12632000 (beats 23%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def numMusicPlaylists(self, n, goal, k):
        """
        :type n: int
        :type goal: int
        :type k: int
        :rtype: int
        """
        MOD = 10**9 + 7
        
        # dp[i][j]: number of playlists of length i with j unique songs
        dp = [[0] * (n + 1) for _ in range(goal + 1)]
        dp[0][0] = 1

        for i in range(1, goal + 1):
            for j in range(1, min(i, n) + 1):
                # 1. Play a new unique song: (n - (j - 1)) choices
                dp[i][j] = (dp[i][j] + dp[i - 1][j - 1] * (n - j + 1)) % MOD

                # 2. Replay an old song (valid only if j > k): (j - k) choices
                if j > k:
                    dp[i][j] = (dp[i][j] + dp[i - 1][j] * (j - k)) % MOD

        return dp[goal][n]