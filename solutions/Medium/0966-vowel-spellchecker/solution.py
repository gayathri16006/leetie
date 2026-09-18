# ──────────────────────────────────────────────────
# Problem  : 966. Vowel Spellchecker
# Difficulty: Medium
# Tags     : Array, Hash Table, String
# Link     : https://leetcode.com/problems/vowel-spellchecker/
# Runtime  : 79 ms (beats 30%)
# Memory   : 14392000 (beats 28%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def spellchecker(self, wordlist, queries):
        """
        :type wordlist: List[str]
        :type queries: List[str]
        :rtype: List[str]
        """
        exact_words = set(wordlist)
        case_map = {}
        vowel_map = {}

        def devowel(word):
            return "".join("*" if c in "aeiou" else c for c in word.lower())

        for word in wordlist:
            lower = word.lower()
            pattern = devowel(word)

            if lower not in case_map:
                case_map[lower] = word
            if pattern not in vowel_map:
                vowel_map[pattern] = word

        ans = []
        for q in queries:
            if q in exact_words:
                ans.append(q)
            elif q.lower() in case_map:
                ans.append(case_map[q.lower()])
            elif devowel(q) in vowel_map:
                ans.append(vowel_map[devowel(q)])
            else:
                ans.append("")

        return ans