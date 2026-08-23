# ──────────────────────────────────────────────────
# Problem  : 600. Non-negative Integers without Consecutive Ones
# Difficulty: Hard
# Tags     : Dynamic Programming
# Link     : https://leetcode.com/problems/non-negative-integers-without-consecutive-ones/
# Runtime  : 0 ms (beats 0%)
# Memory   : 19368000 (beats 0%)
# Language : python3
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def findIntegers(self, n: int) -> int:
        """
        :type n: int
        :rtype: int
        """
        # Precompute Fibonacci array where f[i] = number of valid binary strings of length i
        # 31 bits are sufficient since n <= 10^9 < 2^30
        f = [0] * 32
        f[0] = 1
        f[1] = 2
        for i in range(2, 32):
            f[i] = f[i - 1] + f[i - 2]
        
        binary = bin(n)[2:]
        length = len(binary)
        
        ans = 0
        prev_bit = '0'
        
        for i in range(length):
            if binary[i] == '1':
                # If we choose '0' at this position instead of '1',
                # remaining (length - 1 - i) positions can be filled freely with valid sequences
                ans += f[length - 1 - i]
                
                if prev_bit == '1':
                    # Consecutive '1's found in n's prefix, cannot proceed further
                    return ans
                prev_bit = '1'
            else:
                prev_bit = '0'
                
        # If n itself contains no consecutive ones, count n
        return ans + 1