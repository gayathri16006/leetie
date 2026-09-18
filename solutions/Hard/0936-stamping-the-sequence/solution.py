# ──────────────────────────────────────────────────
# Problem  : 936. Stamping The Sequence
# Difficulty: Hard
# Tags     : String, Stack, Greedy, Queue
# Link     : https://leetcode.com/problems/stamping-the-sequence/
# Runtime  : 91 ms (beats 81%)
# Memory   : 12520000 (beats 22%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def movesToStamp(self, stamp, target):
        """
        :type stamp: str
        :type target: str
        :rtype: List[int]
        """
        s_len, t_len = len(stamp), len(target)
        target = list(target)
        ans = []
        total_stamped = [0]
        visited = [False] * (t_len - s_len + 1)

        def can_stamp(i):
            changed = False
            for j in range(s_len):
                if target[i + j] == '?':
                    continue
                if target[i + j] != stamp[j]:
                    return False
                changed = True
            return changed

        def do_stamp(i):
            count = 0
            for j in range(s_len):
                if target[i + j] != '?':
                    target[i + j] = '?'
                    count += 1
            return count

        while total_stamped[0] < t_len:
            stamped_this_round = False
            for i in range(t_len - s_len + 1):
                if not visited[i] and can_stamp(i):
                    total_stamped[0] += do_stamp(i)
                    visited[i] = True
                    stamped_this_round = True
                    ans.append(i)
                    if total_stamped[0] == t_len:
                        break

            if not stamped_this_round:
                return []

        return ans[::-1]