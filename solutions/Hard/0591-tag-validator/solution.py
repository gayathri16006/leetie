# ──────────────────────────────────────────────────
# Problem  : 591. Tag Validator
# Difficulty: Hard
# Tags     : String, Stack
# Link     : https://leetcode.com/problems/tag-validator/
# Runtime  : 0 ms (beats 0%)
# Memory   : 12212000 (beats 0%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

import re

class Solution(object):
    def isValid(self, code):
        """
        :type code: str
        :rtype: bool
        """
        # Replace CDATA blocks first (must be inside tags, handled during linear scan or regex parsing)
        # Using a stack-based parser to properly check valid nesting and wrapping rules:
        
        stack = []
        i = 0
        n = len(code)
        
        while i < n:
            # If stack is empty after processing some tags, subsequent content is invalid
            if i > 0 and not stack:
                return False
            
            # Check for CDATA: <![CDATA[...]]>
            if code.startswith("<![CDATA[", i):
                if not stack:
                    return False
                cdata_end = code.find("]]>", i + 9)
                if cdata_end == -1:
                    return False
                i = cdata_end + 3
                
            # Check for Closing Tag: </TAG_NAME>
            elif code.startswith("</", i):
                close_end = code.find(">", i + 2)
                if close_end == -1:
                    return False
                tag_name = code[i + 2:close_end]
                if not (1 <= len(tag_name) <= 9 and tag_name.isupper()):
                    return False
                if not stack or stack[-1] != tag_name:
                    return False
                stack.pop()
                i = close_end + 1
                
            # Check for Opening Tag: <TAG_NAME>
            elif code.startswith("<", i):
                open_end = code.find(">", i + 1)
                if open_end == -1:
                    return False
                tag_name = code[i + 1:open_end]
                if not (1 <= len(tag_name) <= 9 and tag_name.isupper()):
                    return False
                stack.append(tag_name)
                i = open_end + 1
                
            # Plain text character
            else:
                if not stack:
                    return False
                i += 1
                
        return len(stack) == 0