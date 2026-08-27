# ──────────────────────────────────────────────────
# Problem  : 726. Number of Atoms
# Difficulty: Hard
# Tags     : Hash Table, String, Stack, Sorting
# Link     : https://leetcode.com/problems/number-of-atoms/
# Runtime  : 0 ms (beats 100%)
# Memory   : 19460000 (beats 39%)
# Language : python3
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

from collections import defaultdict

class Solution:
    def countOfAtoms(self, formula: str) -> str:
        stack = [defaultdict(int)]
        i = 0
        n = len(formula)
        
        while i < n:
            if formula[i] == '(':
                stack.append(defaultdict(int))
                i += 1
            elif formula[i] == ')':
                i += 1
                start = i
                while i < n and formula[i].isdigit():
                    i += 1
                multiplier = int(formula[start:i]) if start < i else 1
                
                top = stack.pop()
                for atom, count in top.items():
                    stack[-1][atom] += count * multiplier
            else:
                # Parse atom name
                start = i
                i += 1
                while i < n and formula[i].islower():
                    i += 1
                atom = formula[start:i]
                
                # Parse count
                start = i
                while i < n and formula[i].isdigit():
                    i += 1
                count = int(formula[start:i]) if start < i else 1
                
                stack[-1][atom] += count
                
        final_counts = stack[0]
        res = []
        for atom in sorted(final_counts.keys()):
            res.append(atom)
            if final_counts[atom] > 1:
                res.append(str(final_counts[atom]))
                
        return "".join(res)