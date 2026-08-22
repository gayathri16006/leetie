# ──────────────────────────────────────────────────
# Problem  : 468. Validate IP Address
# Difficulty: Medium
# Tags     : String
# Link     : https://leetcode.com/problems/validate-ip-address/
# Runtime  : 0 ms (beats 100%)
# Memory   : 12344000 (beats 67%)
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
            if not chunk or len(chunk) > 3:
                return False
            if not chunk.isdigit():
                return False
            if chunk[0] == '0' and len(chunk) > 1:
                return False
            if not (0 <= int(chunk) <= 255):
                return False
        return True

    def _validate_ipv6(self, ip):
        chunks = ip.split(':')
        hex_digits = set("0123456789abcdefABCDEF")
        for chunk in chunks:
            if not chunk or len(chunk) > 4:
                return False
            if not all(c in hex_digits for c in chunk):
                return False
        return True