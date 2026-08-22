# ──────────────────────────────────────────────────
# Problem  : 482. License Key Formatting
# Difficulty: Easy
# Tags     : String
# Link     : https://leetcode.com/problems/license-key-formatting/
# Runtime  : 0 ms (beats 0%)
# Memory   : 12460000 (beats 0%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def licenseKeyFormatting(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        # Clean string: remove dashes and convert to uppercase
        clean = s.replace("-", "").upper()
        
        if not clean:
            return ""
        
        # Determine the length of the very first group
        first_group_len = len(clean) % k
        
        parts = []
        
        # If there's a non-empty first group, add it
        if first_group_len > 0:
            parts.append(clean[:first_group_len])
            
        # Add all subsequent full groups of size k
        for i in range(first_group_len, len(clean), k):
            parts.append(clean[i:i + k])
            
        return "-".join(parts)