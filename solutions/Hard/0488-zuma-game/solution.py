# ──────────────────────────────────────────────────
# Problem  : 488. Zuma Game
# Difficulty: Hard
# Tags     : String, Dynamic Programming, Stack, Breadth-First Search, Memoization
# Link     : https://leetcode.com/problems/zuma-game/
# Runtime  : 46 ms (beats 0%)
# Memory   : 12700000 (beats 0%)
# Language : python
# Copyright: (c) 2026 gayathri16006. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

from collections import Counter
import re

class Solution(object):
    def findMinStep(self, board, hand):
        """
        :type board: str
        :type hand: str
        :rtype: int
        """
        def clean(s):
            # Recursively eliminate 3 or more consecutive identical balls
            n = -1
            while len(s) != n:
                n = len(s)
                s = re.sub(r'([A-Z])\1{2,}', '', s)
            return s

        memo = {}
        hand_count = Counter(hand)

        def dfs(curr_board, hand_map):
            if not curr_board:
                return 0

            state = (curr_board, tuple(sorted(hand_map.items())))
            if state in memo:
                return memo[state]

            res = float('inf')

            for i in range(len(curr_board) + 1):
                for color in list(hand_map.keys()):
                    if hand_map[color] == 0:
                        continue

                    # Pruning: Only insert adjacent to the same color,
                    # or between two identical balls of a different color
                    should_insert = False
                    if i > 0 and curr_board[i - 1] == color:
                        should_insert = True
                    elif i < len(curr_board) and curr_board[i] == color:
                        should_insert = True
                    elif 0 < i < len(curr_board) and curr_board[i - 1] == curr_board[i]:
                        should_insert = True

                    if not should_insert:
                        continue

                    # Make move
                    hand_map[color] -= 1
                    next_board = clean(curr_board[:i] + color + curr_board[i:])
                    
                    sub = dfs(next_board, hand_map)
                    if sub != float('inf'):
                        res = min(res, 1 + sub)
                    
                    # Backtrack
                    hand_map[color] += 1

            memo[state] = res
            return res

        ans = dfs(board, hand_count)
        return ans if ans != float('inf') else -1