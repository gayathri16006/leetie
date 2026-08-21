# ──────────────────────────────────────────────────
# Problem  : 393. UTF-8 Validation
# Difficulty: Medium
# Tags     : Array, Bit Manipulation
# Link     : https://leetcode.com/problems/utf-8-validation/
# Runtime  : 3 ms (beats 65%)
# Memory   : 12604000 (beats 38%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        remaining_bytes = 0
        
        for num in data:
            # Mask to keep only the least significant 8 bits
            byte = num & 0xFF
            
            if remaining_bytes == 0:
                # Check how many bytes this character starts with
                if (byte >> 7) == 0b0:
                    remaining_bytes = 0
                elif (byte >> 5) == 0b110:
                    remaining_bytes = 1
                elif (byte >> 4) == 0b1110:
                    remaining_bytes = 2
                elif (byte >> 3) == 0b11110:
                    remaining_bytes = 3
                else:
                    # Invalid leading byte prefix
                    return False
            else:
                # Continuation bytes must start with '10'
                if (byte >> 6) != 0b10:
                    return False
                remaining_bytes -= 1
                
        return remaining_bytes == 0