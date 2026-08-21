# ──────────────────────────────────────────────────
# Problem  : 388. Longest Absolute File Path
# Difficulty: Medium
# Tags     : String, Stack, Depth-First Search
# Link     : https://leetcode.com/problems/longest-absolute-file-path/
# Runtime  : 0 ms (beats 100%)
# Memory   : 12340000 (beats 59%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        max_length = 0
        # Map depth level -> cumulative path length up to that level
        # depth 0 has base length 0 (no characters, no slash)
        path_lengths = {0: 0}
        
        for line in input.split('\n'):
            name = line.lstrip('\t')
            depth = len(line) - len(name)
            
            if '.' in name:
                # It's a file: compute total length with current path + filename
                total_len = path_lengths[depth] + len(name)
                max_length = max(max_length, total_len)
            else:
                # It's a directory: update length at (depth + 1), +1 for the '/' separator
                path_lengths[depth + 1] = path_lengths[depth] + len(name) + 1
                
        return max_length