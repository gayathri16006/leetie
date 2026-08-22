# ──────────────────────────────────────────────────
# Problem  : 472. Concatenated Words
# Difficulty: Hard
# Tags     : Array, String, Dynamic Programming, Depth-First Search, Trie, Sorting
# Link     : https://leetcode.com/problems/concatenated-words/
# Runtime  : 359 ms (beats 38%)
# Memory   : 14444000 (beats 85%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):

    def findAllConcatenatedWordsInADict(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        word_set = set(words)
        result = []

        def can_form(word):
            # Dynamic programming / Memoization table (similar to Word Break)
            n = len(word)
            dp = [False] * (n + 1)
            dp[0] = True

            for i in range(1, n + 1):
                for j in range(i):
                    # Condition: prefix can be formed, remaining substring is in dictionary,
                    # and the substring is not the whole word itself (needs at least 2 words)
                    if (
                        dp[j]
                        and word[j:i] in word_set
                        and not (j == 0 and i == n)
                    ):
                        dp[i] = True
                        break

            return dp[n]

        for word in words:
            if not word:
                continue
            if can_form(word):
                result.append(word)

        return result