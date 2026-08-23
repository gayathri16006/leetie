# ──────────────────────────────────────────────────
# Problem  : 564. Find the Closest Palindrome
# Difficulty: Hard
# Tags     : Math, String
# Link     : https://leetcode.com/problems/find-the-closest-palindrome/
# Runtime  : 4 ms (beats 8%)
# Memory   : 12484000 (beats 26%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def nearestPalindromic(self, n):
        L = len(n)
        num = int(n)
        
        # Edge cases: 0 to 10
        if num <= 10:
            return str(num - 1)
        if num == 11:
            return "9"
            
        candidates = set()
        
        # Candidate 4 & 5: Edge boundary cases (e.g., 999..999 or 100..001)
        candidates.add(10**(L - 1) - 1)
        candidates.add(10**L + 1)
        
        # Extract the prefix (first half, including middle character if odd length)
        prefix_len = (L + 1) // 2
        prefix = int(n[:prefix_len])
        
        # Candidate 1, 2, 3: prefix, prefix + 1, prefix - 1
        for diff in (-1, 0, 1):
            p = str(prefix + diff)
            if L % 2 == 0:
                pal = p + p[::-1]
            else:
                pal = p + p[:-1][::-1]
            candidates.add(int(pal))
            
        # Remove the original number
        candidates.discard(num)
        
        # Find candidate with minimum absolute difference; tie-break with smaller value
        closest = min(candidates, key=lambda x: (abs(x - num), x))
        
        return str(closest)