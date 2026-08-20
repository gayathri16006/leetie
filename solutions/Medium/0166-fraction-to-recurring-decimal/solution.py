# ──────────────────────────────────────────────────
# Problem  : 166. Fraction to Recurring Decimal
# Difficulty: Medium
# Tags     : Hash Table, Math, String
# Link     : https://leetcode.com/problems/fraction-to-recurring-decimal/
# Runtime  : 0 ms (beats 100%)
# Memory   : 12424000 (beats 48%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if numerator == 0:
            return "0"
        
        result = []
        
        # Handle sign
        if (numerator < 0) ^ (denominator < 0):
            result.append("-")
            
        num = abs(numerator)
        den = abs(denominator)
        
        # Integer part
        result.append(str(num // den))
        remainder = num % den
        
        # If no fractional part exists
        if remainder == 0:
            return "".join(result)
        
        result.append(".")
        remainder_map = {}
        
        # Fractional part
        while remainder != 0:
            if remainder in remainder_map:
                insert_idx = remainder_map[remainder]
                result.insert(insert_idx, "(")
                result.append(")")
                break
                
            remainder_map[remainder] = len(result)
            remainder *= 10
            result.append(str(remainder // den))
            remainder %= den
            
        return "".join(result)