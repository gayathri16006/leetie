# ──────────────────────────────────────────────────
# Problem  : 929. Unique Email Addresses
# Difficulty: Easy
# Tags     : Array, Hash Table, String
# Link     : https://leetcode.com/problems/unique-email-addresses/
# Runtime  : 0 ms (beats 0%)
# Memory   : 12260000 (beats 0%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        unique_emails = set()
        
        for email in emails:
            local, domain = email.split('@')
            
            # Ignore everything after the first '+' in the local name
            local = local.split('+')[0]
            
            # Remove all '.' from the local name
            local = local.replace('.', '')
            
            # Add normalized email to set
            unique_emails.add(local + '@' + domain)
            
        return len(unique_emails)