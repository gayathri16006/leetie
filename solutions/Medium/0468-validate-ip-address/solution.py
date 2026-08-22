# ──────────────────────────────────────────────────
# Problem  : 468. Validate IP Address
# Difficulty: Medium
# Tags     : String
# Link     : https://leetcode.com/problems/validate-ip-address/
# Runtime  : 0 ms (beats 0%)
# Memory   : 12540000 (beats 0%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def validIPAddress(self, queryIP):
        """
        :type queryIP: str
        :rtype: str
        """
        if queryIP.count('.') == 3:
            return "IPv4" if self._validate_ipv4(queryIP) else "Neither"
        elif queryIP.count(':') == 7:
            return "IPv6" if self._validate_ipv6(queryIP) else "Neither"
        return "Neither"

    def _validate_ipv4(self, ip):
        chunks = ip.split('.')
        for chunk in chunks:
            # Length must be between 1 and 3, and only contain digits
            if not chunk or len(chunk) > 3 or not chunk.isdigit():
                return False
            # Check for leading zeros (e.g., '01', '00')
            if chunk[0] == '0' and len(chunk) > 1:
                return False
            # Value must be in range [0, 255]
            if not (0 <= int(chunk) <= 255):
                return False
        return True

    def _validate_ipv6(self, ip):
        chunks = ip.split(':')
        hex_digits = set("0123456789abcdefABCDEF")
        for chunk in chunks:
            # Length must be between 1 and 4, only hex characters
            if not chunk or len(chunk) > 4:
                return False
            if not all(c in hex_digits for c in chunk):
                return False
        return True