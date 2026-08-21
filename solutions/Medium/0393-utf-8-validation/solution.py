# ──────────────────────────────────────────────────
# Problem  : 393. UTF-8 Validation
# Difficulty: Medium
# Tags     : Array, Bit Manipulation
# Link     : https://leetcode.com/problems/utf-8-validation/
# Runtime  : 0 ms (beats 100%)
# Memory   : 12636000 (beats 38%)
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
        # Number of continuation bytes expected for the current character
        remaining_bytes = 0
        
        for num in data:
            # We only care about the least significant 8 bits
            byte = num & 0xFF
            
            if remaining_bytes == 0:
                # Determine how many bytes the character consists of
                if (byte >> 7) == 0b0:
                    remaining_bytes = 0
                elif (byte >> 5) == 0b110:
                    remaining_bytes = 1
                elif (byte >> 4) == 0b1110:
                    remaining_bytes = 2
                elif (byte >> 3) == 0b11110:
                    remaining_bytes = 3
                else:
                    # Invalid prefix (e.g., 10xxxxxx as start byte or > 4 bytes)
                    return False
            else:
                # Continuation byte must start with binary '10'
                if (byte >> 6) != 0b10:
                    return False
                remaining_bytes -= 1
                
        # Valid UTF-8 must not have any pending continuation bytes
        return remaining_bytes == 0