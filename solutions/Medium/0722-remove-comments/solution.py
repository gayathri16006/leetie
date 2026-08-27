# ──────────────────────────────────────────────────
# Problem  : 722. Remove Comments
# Difficulty: Medium
# Tags     : Array, String
# Link     : https://leetcode.com/problems/remove-comments/
# Runtime  : 0 ms (beats 100%)
# Memory   : 19408000 (beats 14%)
# Language : python3
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def removeComments(self, source: list[str]) -> list[str]:
        in_block = False
        res = []
        new_line = []

        for line in source:
            i = 0
            n = len(line)
            while i < n:
                if in_block:
                    # Look for end of block comment
                    if i + 1 < n and line[i:i + 2] == "*/":
                        in_block = False
                        i += 1
                else:
                    # Look for start of block comment
                    if i + 1 < n and line[i:i + 2] == "/*":
                        in_block = True
                        i += 1
                    # Look for line comment (ignore remainder of line)
                    elif i + 1 < n and line[i:i + 2] == "//":
                        break
                    else:
                        new_line.append(line[i])
                i += 1

            # Only append the line if we are not inside an unfinished block comment and line is non-empty
            if not in_block and new_line:
                res.append("".join(new_line))
                new_line = []

        return res