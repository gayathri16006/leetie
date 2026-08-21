# ──────────────────────────────────────────────────
# Problem  : 68. Text Justification
# Difficulty: Hard
# Tags     : Array, String, Simulation
# Link     : https://leetcode.com/problems/text-justification/
# Runtime  : 0 ms (beats 100%)
# Memory   : 12456000 (beats 24%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        res = []
        cur_line = []
        num_of_letters = 0

        for word in words:
            # Check if adding the word exceeds maxWidth:
            # num_of_letters + len(word) + minimum 1 space per word gap (len(cur_line))
            if num_of_letters + len(word) + len(cur_line) > maxWidth:
                # Distribute spaces among cur_line words
                total_spaces = maxWidth - num_of_letters
                gaps = len(cur_line) - 1

                if gaps == 0:
                    # Single word in line: left-justify
                    res.append(cur_line[0] + " " * total_spaces)
                else:
                    space_per_gap = total_spaces // gaps
                    extra_spaces = total_spaces % gaps

                    line = []
                    for i in range(gaps):
                        line.append(cur_line[i])
                        # Distribute the base spaces plus 1 extra space to the leftmost slots
                        line.append(" " * (space_per_gap + (1 if i < extra_spaces else 0)))
                    line.append(cur_line[-1])
                    res.append("".join(line))

                # Reset buffer for new line
                cur_line = []
                num_of_letters = 0

            cur_line.append(word)
            num_of_letters += len(word)

        # Handle the last line (left-justified, separated by single space, padded at the end)
        last_line = " ".join(cur_line)
        last_line += " " * (maxWidth - len(last_line))
        res.append(last_line)

        return res