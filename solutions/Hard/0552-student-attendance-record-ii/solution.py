# ──────────────────────────────────────────────────
# Problem  : 552. Student Attendance Record II
# Difficulty: Hard
# Tags     : Dynamic Programming
# Link     : https://leetcode.com/problems/student-attendance-record-ii/
# Runtime  : 3625 ms (beats 54%)
# Memory   : 15480000 (beats 73%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def checkRecord(self, n):
        MOD = 10**9 + 7
        
        # dp[a][l] represents count of valid sequences with:
        # a: count of 'A's (0 or 1)
        # l: count of trailing 'L's (0, 1, or 2)
        dp = [[0] * 3 for _ in range(2)]
        dp[0][0] = 1  # Base case: empty sequence of length 0
        
        for _ in range(n):
            next_dp = [[0] * 3 for _ in range(2)]
            
            for a in range(2):
                for l in range(3):
                    val = dp[a][l]
                    if val == 0:
                        continue
                    
                    # 1. Append 'P' -> resets late count to 0
                    next_dp[a][0] = (next_dp[a][0] + val) % MOD
                    
                    # 2. Append 'A' -> increments 'A' count, resets late count to 0
                    if a == 0:
                        next_dp[1][0] = (next_dp[1][0] + val) % MOD
                        
                    # 3. Append 'L' -> increments late count
                    if l < 2:
                        next_dp[a][l + 1] = (next_dp[a][l + 1] + val) % MOD
                        
            dp = next_dp
            
        # Sum all valid terminal states
        total = 0
        for a in range(2):
            for l in range(3):
                total = (total + dp[a][l]) % MOD
                
        return total