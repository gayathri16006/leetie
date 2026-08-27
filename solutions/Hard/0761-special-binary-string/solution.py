# ──────────────────────────────────────────────────
# Problem  : 761. Special Binary String
# Difficulty: Hard
# Tags     : String, Divide and Conquer, Sorting
# Link     : https://leetcode.com/problems/special-binary-string/
# Runtime  : 0 ms (beats 0%)
# Memory   : 19152000 (beats 0%)
# Language : python3
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        count = 0
        i = 0
        res = []
        
        for j, char in enumerate(s):
            count += 1 if char == '1' else -1
            # Found a primitive special substring
            if count == 0:
                # Recursively maximize the inner component and wrap with '1' and '0'
                res.append('1' + self.makeLargestSpecial(s[i + 1:j]) + '0')
                i = j + 1
                
        # Sort sub-parts in descending order to achieve the lexicographically largest result
        res.sort(reverse=True)
        return "".join(res)