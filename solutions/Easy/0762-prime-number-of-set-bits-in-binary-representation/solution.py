# ──────────────────────────────────────────────────
# Problem  : 762. Prime Number of Set Bits in Binary Representation
# Difficulty: Easy
# Tags     : Math, Bit Manipulation, Primality Test
# Link     : https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/
# Runtime  : 0 ms (beats 0%)
# Memory   : 19396000 (beats 0%)
# Language : python3
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        # Since right <= 10^6 < 2^20, the maximum number of set bits is < 20.
        # Primes less than 20:
        primes = {2, 3, 5, 7, 11, 13, 17, 19}
        
        count = 0
        for num in range(left, right + 1):
            if num.bit_count() in primes:
                count += 1
                
        return count