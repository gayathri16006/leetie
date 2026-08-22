# ──────────────────────────────────────────────────
# Problem  : 466. Count The Repetitions
# Difficulty: Hard
# Tags     : Two Pointers, String, Dynamic Programming
# Link     : https://leetcode.com/problems/count-the-repetitions/
# Runtime  : 0 ms (beats 0%)
# Memory   : 12396000 (beats 0%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def getMaxRepetitions(self, s1, n1, s2, n2):
        """
        :type s1: str
        :type n1: int
        :type s2: str
        :type n2: int
        :rtype: int
        """
        # Quick check: ensure all characters in s2 exist in s1
        if not set(s2).issubset(set(s1)):
            return 0

        # s2_idx_history[index_in_s2] = (s1_count, s2_count)
        s2_idx_history = {}
        
        s1_count = 0
        s2_count = 0
        index_in_s2 = 0
        len_s2 = len(s2)

        while s1_count < n1:
            s1_count += 1
            
            for ch in s1:
                if ch == s2[index_in_s2]:
                    index_in_s2 += 1
                    if index_in_s2 == len_s2:
                        s2_count += 1
                        index_in_s2 = 0
            
            # Check if we have seen this index_in_s2 after finishing an s1 block
            if index_in_s2 in s2_idx_history:
                prev_s1_count, prev_s2_count = s2_idx_history[index_in_s2]
                
                # Cycle properties
                cycle_s1_len = s1_count - prev_s1_count
                cycle_s2_len = s2_count - prev_s2_count
                
                # Fast forward through remaining full cycles
                remaining_s1 = n1 - s1_count
                num_cycles = remaining_s1 // cycle_s1_len
                
                s1_count += num_cycles * cycle_s1_len
                s2_count += num_cycles * cycle_s2_len
                
                # Clear history to avoid re-triggering cycle jump during leftover steps
                s2_idx_history.clear()
            else:
                s2_idx_history[index_in_s2] = (s1_count, s2_count)

        return s2_count // n2