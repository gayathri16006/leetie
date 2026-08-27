# ──────────────────────────────────────────────────
# Problem  : 770. Basic Calculator IV
# Difficulty: Hard
# Tags     : Hash Table, Math, String, Stack, Recursion
# Link     : https://leetcode.com/problems/basic-calculator-iv/
# Runtime  : 7 ms (beats 30%)
# Memory   : 19776000 (beats 61%)
# Language : python3
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

import collections

class Poly(collections.Counter):
    def __add__(self, other):
        res = Poly(self)
        for term, coeff in other.items():
            res[term] += coeff
        return res

    def __sub__(self, other):
        res = Poly(self)
        for term, coeff in other.items():
            res[term] -= coeff
        return res

    def __mul__(self, other):
        res = Poly()
        for t1, c1 in self.items():
            for t2, c2 in other.items():
                # Merge and sort the tuple representing the variable products
                merged_term = tuple(sorted(t1 + t2))
                res[merged_term] += c1 * c2
        return res

    def evaluate(self, env):
        res = Poly()
        for term, coeff in self.items():
            current_coeff = coeff
            remaining_vars = []
            for var in term:
                if var in env:
                    current_coeff *= env[var]
                else:
                    remaining_vars.append(var)
            res[tuple(sorted(remaining_vars))] += current_coeff
        return res

    def to_list(self):
        # Sort terms: highest degree first, then lexicographically by variable names
        sorted_terms = sorted(self.keys(), key=lambda t: (-len(t), t))
        res = []
        for term in sorted_terms:
            coeff = self[term]
            if coeff != 0:
                if not term:
                    res.append(str(coeff))
                else:
                    res.append(f"{coeff}*" + "*".join(term))
        return res


class Solution:
    def basicCalculatorIV(self, expression: str, evalvars: list[str], evalints: list[int]) -> list[str]:
        env = dict(zip(evalvars, evalints))
        
        # Tokenize expression
        tokens = []
        i = 0
        n = len(expression)
        while i < n:
            if expression[i] == ' ':
                i += 1
            elif expression[i] in '()+-*':
                tokens.append(expression[i])
                i += 1
            else:
                j = i
                while j < n and expression[j] not in ' ()+-*':
                    j += 1
                tokens.append(expression[i:j])
                i = j

        def compute(op, p2, p1):
            if op == '+': return p1 + p2
            if op == '-': return p1 - p2
            if op == '*': return p1 * p2

        # Standard Shunting-Yard parsing for polynomials
        prec = {'+': 1, '-': 1, '*': 2}
        values = []
        ops = []

        def apply_top_op():
            op = ops.pop()
            p2 = values.pop()
            p1 = values.pop()
            values.append(compute(op, p2, p1))

        for token in tokens:
            if token.isdigit():
                p = Poly()
                p[()] = int(token)
                values.append(p)
            elif token.isalpha():
                p = Poly()
                p[(token,)] = 1
                values.append(p)
            elif token == '(':
                ops.append(token)
            elif token == ')':
                while ops and ops[-1] != '(':
                    apply_top_op()
                ops.pop() # Pop '('
            else:
                while ops and ops[-1] != '(' and prec.get(ops[-1], 0) >= prec.get(token, 0):
                    apply_top_op()
                ops.append(token)

        while ops:
            apply_top_op()

        result_poly = values[0].evaluate(env)
        return result_poly.to_list()