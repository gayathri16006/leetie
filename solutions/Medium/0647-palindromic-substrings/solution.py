# ──────────────────────────────────────────────────
# Problem  : 647. Palindromic Substrings
# Difficulty: Medium
# Tags     : Two Pointers, String, Dynamic Programming
# Link     : https://leetcode.com/problems/palindromic-substrings/
# Runtime  : 0 ms (beats 0%)
# Memory   : 19328000 (beats 0%)
# Language : python3
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        total_count = 0
        
        def expand_around_center(left: int, right: int) -> int:
            count = 0
            while left >= 0 and right < n and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
            return count

        for i in range(n):
            # Odd-length palindromes (single-character centers)
            total_count += expand_around_center(i, i)
            # Even-length palindromes (two-character centers)
            total_count += expand_around_center(i, i + 1)
            
        return total_count