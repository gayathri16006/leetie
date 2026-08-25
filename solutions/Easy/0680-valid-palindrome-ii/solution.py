# ──────────────────────────────────────────────────
# Problem  : 680. Valid Palindrome II
# Difficulty: Easy
# Tags     : Two Pointers, String, Greedy
# Link     : https://leetcode.com/problems/valid-palindrome-ii/
# Runtime  : 0 ms (beats 0%)
# Memory   : 19308000 (beats 0%)
# Language : python3
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def validPalindrome(self, s: str) -> bool:
        def check_palindrome(l: int, r: int) -> bool:
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        left, right = 0, len(s) - 1
        
        while left < right:
            if s[left] != s[right]:
                # Try skipping s[left] OR skipping s[right]
                return check_palindrome(left + 1, right) or check_palindrome(left, right - 1)
            left += 1
            right -= 1
            
        return True