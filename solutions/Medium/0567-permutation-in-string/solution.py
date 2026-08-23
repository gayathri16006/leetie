# ──────────────────────────────────────────────────
# Problem  : 567. Permutation in String
# Difficulty: Medium
# Tags     : Hash Table, Two Pointers, String, Sliding Window
# Link     : https://leetcode.com/problems/permutation-in-string/
# Runtime  : 15 ms (beats 99%)
# Memory   : 12876000 (beats 18%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def checkInclusion(self, s1, s2):
        l1, l2 = len(s1), len(s2)
        if l1 > l2:
            return False
        
        count1 = [0] * 26
        count2 = [0] * 26
        
        # Initialize frequencies for s1 and the first window of s2
        for i in range(l1):
            count1[ord(s1[i]) - ord('a')] += 1
            count2[ord(s2[i]) - ord('a')] += 1
            
        if count1 == count2:
            return True
            
        # Slide the window across s2
        for i in range(l1, l2):
            count2[ord(s2[i]) - ord('a')] += 1             # Add incoming character
            count2[ord(s2[i - l1]) - ord('a')] -= 1        # Remove outgoing character
            
            if count1 == count2:
                return True
                
        return False