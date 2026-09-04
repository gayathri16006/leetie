# ──────────────────────────────────────────────────
# Problem  : 842. Split Array into Fibonacci Sequence
# Difficulty: Medium
# Tags     : String, Backtracking
# Link     : https://leetcode.com/problems/split-array-into-fibonacci-sequence/
# Runtime  : 12 ms (beats 39%)
# Memory   : 12564000 (beats 7%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def splitIntoFibonacci(self, num):
        """
        :type num: str
        :rtype: List[int]
        """
        MAX_INT = 2**31 - 1
        n = len(num)
        ans = []

        def backtrack(index):
            if index == n:
                return len(ans) >= 3

            curr = 0
            for i in range(index, n):
                # Avoid multi-digit numbers with leading zero
                if i > index and num[index] == '0':
                    break

                curr = curr * 10 + int(num[i])
                if curr > MAX_INT:
                    break

                # If we have at least 2 numbers, check Fibonacci condition
                if len(ans) >= 2:
                    expected = ans[-1] + ans[-2]
                    if curr < expected:
                        continue
                    elif curr > expected:
                        break

                ans.append(curr)
                if backtrack(i + 1):
                    return True
                ans.pop()

            return False

        if backtrack(0):
            return ans
        return []