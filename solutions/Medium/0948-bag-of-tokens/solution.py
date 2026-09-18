# ──────────────────────────────────────────────────
# Problem  : 948. Bag of Tokens
# Difficulty: Medium
# Tags     : Array, Two Pointers, Greedy, Sorting
# Link     : https://leetcode.com/problems/bag-of-tokens/
# Runtime  : 0 ms (beats 100%)
# Memory   : 12532000 (beats 17%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def bagOfTokensScore(self, tokens, power):
        """
        :type tokens: List[int]
        :type power: int
        :rtype: int
        """
        tokens.sort()
        left = 0
        right = len(tokens) - 1
        score = 0
        max_score = 0

        while left <= right:
            # Play smallest token face-up if we have enough power
            if power >= tokens[left]:
                power -= tokens[left]
                score += 1
                left += 1
                max_score = max(max_score, score)
            
            elif score > 0:
                power += tokens[right]
                score -= 1
                right -= 1
            else:
                break

        return max_score